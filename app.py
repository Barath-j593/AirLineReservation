import os
import logging
from flask import Flask, render_template, request, jsonify
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail
from datetime import datetime
from recommend import get_recommendations
from utils import send_booking_confirmation, format_price
from extensions import db
import logging

logging.debug("Initializing app.py")

logging.debug("Registering format_price filter")

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the app
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = os.environ.get("SESSION_SECRET", os.urandom(24).hex())
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airlines.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
csrf = CSRFProtect(app)
db.init_app(app)

# Register Jinja2 filters
app.jinja_env.filters['format_price'] = format_price

# Configure login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'airwaysabc@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', 'pyef tixk gwkf padm')
app.config['MAIL_DEFAULT_SENDER'] = 'balakumaran2470050@ssn.edu.in'
mail = Mail(app)

# Import routes after app creation to avoid circular imports
from routes import *  # Explicit import, no wildcard
from booking import register_routes

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))

# Initialize database
with app.app_context():
    db.create_all()

# Register booking routes
register_routes(app)

# Debug routes
with app.test_request_context():
    for rule in app.url_map.iter_rules():
        print(f"Endpoint: {rule.endpoint}, Route: {rule}")

if __name__ == "__main__":
    app.run(debug=True)