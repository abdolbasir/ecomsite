# Django E-commerce Practice Project

A simple e-commerce website built with Django for educational purposes. This project demonstrates the core concepts of Django, including models, views, templates, forms, static and media file handling, and admin customization. It is ideal for new learners who want to understand how to build a basic online store with Django from scratch.

## Features

- Product listing and detail pages
- Shopping cart functionality
- Admin interface customization
- User authentication (login/logout)
- Media and static file management

## Project Structure
ecom-site/

├── ecomsite/ # Main project settings

├── shop/ # Main app with models, views, forms, templates

├── static/ # Static files (CSS, JS, images)

├── media/ # Uploaded media files

├── templates/ # Project-level templates

├── requirements.txt # Python dependencies

├── manage.py # Django management script

└── db.sqlite3 # SQLite database (for development)


## Getting Started

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)
- (Optional but recommended) [virtualenv](https://virtualenv.pypa.io/en/latest/)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ecom-site.git
   cd ecom-site
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the site:**
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
   - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Environment Variables

This project currently does **not** use a `.env` file or environment variables for configuration. All settings (including the secret key and debug mode) are in `ecomsite/settings.py`. For production, you should move sensitive settings to environment variables.

## Dependencies

Main dependencies (see `requirements.txt` for all):

- Django 5.2.4
- django-admin-interface
- django-colorfield
- pillow
- python-slugify

## Customization

- To add products or categories, use the Django admin interface.
- Static files are in the `static/` directory; media uploads go to `media/`.
- Templates can be customized in the `templates/` directory.

## License

This project is for educational purposes. Feel free to use and modify it for your learning!

---

**Happy learning Django!**
