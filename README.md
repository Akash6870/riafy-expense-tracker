# 1. Setup virtual environment
python -m venv venv

# Activate on Windows:
.\venv\Scripts\activate
# Activate on macOS/Linux:
# source venv/bin/activate

# 2. Install core framework
pip install django

# 3. Initialize database migrations
python manage.py makemigrations
python manage.py migrate

# 4. Start the server
python manage.py runserver