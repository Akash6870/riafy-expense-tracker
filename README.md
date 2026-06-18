# Personal Expense Tracker

A lightweight, robust personal expense management application built using Python, Django, and Tailwind CSS.

## Getting Started

### Prerequisites
- Python 3.8 or higher installed on your local machine.

### Installation & Run Steps
Execute the following commands in sequence inside your project root directory:

```bash
## 1. Setup virtual environment
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

## 2. Stack Choices & Tradeoffs

### Backend: Django (Python)
* Choice: Python with Django.
* Why: Django operates on a "batteries-included" philosophy. Its built-in Object-Relational Mapper (ORM) and automated form validation (`ModelForm`) eliminate the need to write raw SQL or custom input sanitization manually.
* Tradeoff: It carries more structural overhead than a micro-framework like Flask or FastAPI, but it maximizes speed and security within a strict 2-hour timeline.

### Frontend: HTML5 + Tailwind CSS (via CDN)
* Choice: Server-rendered Django templates styled with the Tailwind CSS browser script.
* Why: It provides an immediate utility-first styling system without configuring complex Node.js build tools or local package managers (Vite/Webpack), keeping the repository fast to clone and inspect.
* Tradeoff: It relies entirely on an active internet connection to draw layout styles at runtime and downloads a larger bundle file than a tailored, pre-compiled production build.

### Database: SQLite
* Choice: SQLite (Django’s default database engine).
* Why: It operates purely as a self-contained, zero-configuration local file (`db.sqlite3`), fulfilling the local execution constraints of the evaluation smoothly.
* Tradeoff: It does not scale well for massive concurrency or enterprise distribution like PostgreSQL, but it completely removes external database installation friction for the examiner.

---

## 3. What's Done vs. Skipped (And Why)

### What's Done
1. Full CRUD Capabilities: Complete workflows to add, view, edit, and delete expenses using robust backend input forms.
2. Dynamic Content Filtering: Multi-parameter filtration supporting partial text title matches, specific category lookups, and flexible date-range scopes.
3. Live Financial Analytics Dashboard: Real-time summary computing the current month's total spending and breaking it down dynamically by categories using database aggregation (`Sum`).

### What's Skipped (And Why)
1. Authentication & Multi-Tenancy: Intentionally bypassed because the project brief explicitly specified *"Authentication or multi-user support is not cared about."* Omitting this allowed full focus on a bulletproof single-user application core.
2. Automated Test Suite: Omitted due to the strict 2-hour implementation constraint, prioritizing manual validation of core end-to-end user workflows.

---

## 4. Known Rough Edges & Handled Edge Cases

### Known Rough Edges
1. CDN Dependency: The frontend UI relies on an active internet connection to load Tailwind CSS via CDN. In a production environment, Tailwind would be compiled locally.
2. Pagination Constraints: The ledger table displays all expenses on a single page. If a     user inputs thousands of entries, this could cause visual browser lag—an issue easily solved in production using Django's built-in `Paginator`.
3. Hardcoded Currency Symbols: The Indian Rupee currency token (₹) is typed directly into the templates. A true production app would utilize Django's localization utilities (`django.utils.formats`) to adjust formatting dynamically based on client machine locales.

### Edge Cases Handled
1. Empty States: If a filter yields zero results or the database is entirely brand new, the UI automatically replaces the table with an explicit message rather than rendering an empty grid or breaking.
2. Asymmetric Date Filters: The filter logic handles partial data safely; applying a "From" date without a "To" date filters sequentially from that point forward without crashing.
3. Data Type Integrity: Django's `DecimalField` and form-cleansing rules instantly block negative values, invalid characters, or missing fields.