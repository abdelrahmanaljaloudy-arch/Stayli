# Flask Auth Starter (Register + Login + Forgot/Reset)

A minimal, beginner-friendly Flask app that shows **registration**, **login**, and **forgot/reset password**.

## Features
- SQLite database (file `app.db` created on first run)
- Passwords hashed with Werkzeug
- "Forgot password" uses a time-limited token (printed in console for this demo)
- Session-based login/logout

## Quick Start
```bash
# 1) Create & activate a virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run the app
python app.py
# Open http://127.0.0.1:5000/
```

## Environment variables (optional)
- `SECRET_KEY` — random string for sessions and token signing
- `SECURITY_PASSWORD_SALT` — extra salt for reset tokens
- `DATABASE` — path to SQLite DB file

Example (Linux/Mac):
```bash
export SECRET_KEY=$(python -c "import os; print(os.urandom(24).hex())")
export SECURITY_PASSWORD_SALT=$(python -c "import os; print(os.urandom(24).hex())")
python app.py
```

## How "Forgot password" works (in this demo)
- Enter your email on `/forgot`.
- The server prints a reset link in the terminal (instead of sending an email).
- Click the printed link to open `/reset/<token>` and set a new password.

## Notes for learning
- Look at `app.py` to see how forms are handled, how we validate input, and how we hash passwords.
- Try to add more checks (stronger password policy, email confirmation, CSRF protection with Flask-WTF, etc.).
- Replace the console print with a real email (e.g., using Flask-Mail or any email API) when you're ready.
```

Happy hacking!
