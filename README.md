# AirLineReservation

Flask-based airline reservation web app with flight search, booking, admin management, and payment flow.

## Requirements

- Python 3.11 or newer
- A virtual environment is recommended

## Install

From the project root:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run

Start the app from the project root:

```powershell
python main.py
```

You can also run the root shim:

```powershell
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Database

The app uses SQLite and creates tables on startup. To reset and seed the database with sample data, run:

```powershell
python -m airline_reservation.init_db
```

That script drops existing tables, recreates them, and loads sample users and flights.

## Environment variables

Optional settings can be configured before startup:

```powershell
$env:SESSION_SECRET = "a_random_secret"
$env:MAIL_PASSWORD = "your_mail_password"
$env:RAZORPAY_KEY_ID = "your_key_id"
$env:RAZORPAY_KEY_SECRET = "your_key_secret"
```

## Project layout

- `main.py` - entry point for local development
- `app.py` - root shim that imports the package app
- `airline_reservation/` - application package
	- `app.py` - Flask app factory-style setup
	- `routes.py` - view functions and route handlers
	- `forms.py` - Flask-WTF forms
	- `models.py` - SQLAlchemy models
	- `data.py` - database helpers and sample data
	- `utils.py` - formatting and email helpers
	- `init_db.py` - database reset/seed script

## Notes

- Templates are stored in the top-level `templates/` folder.
- Static files are stored in the top-level `static/` folder.
- The package app is configured to use those top-level folders directly.
