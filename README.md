# Personal Expense Tracker

A lightweight, robust personal expense management application built using Python, Django, and Tailwind CSS.

## Getting Started

### Prerequisites
- Python 3.8 or higher installed on your local machine.

### Installation & Run Steps
Execute the following commands in sequence inside your project root directory:

```bash
# 1. Setup virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 2. Install core framework
pip install django

# 3. Initialize database migrations
python manage.py makemigrations
python manage.py migrate

# 4. Start the server
python manage.py runserver