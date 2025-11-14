<div align="center">

# 🚀 BusinessPro - Professional Business Website

### *Your trusted partner for professional business solutions*

A modern, feature-rich business website built with Django that provides a complete solution for showcasing services, managing customer inquiries, and handling user authentication. Perfect for small to medium-sized businesses looking to establish a professional online presence.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2.7-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)

[🌐 Live Demo](#) • [📖 Documentation](#-table-of-contents) • [🚀 Quick Start](#-installation) • [📸 Screenshots](#-screenshots)

---

### 🎯 Quick Preview

<table>
  <tr>
    <td width="50%">
      <img src="https://raw.githubusercontent.com/rehansheikhcareer1/Business-Website/main/screenshots/home.png" alt="Homepage"/>
      <p align="center"><b>Modern Homepage</b></p>
    </td>
    <td width="50%">
      <img src="https://raw.githubusercontent.com/rehansheikhcareer1/Business-Website/main/screenshots/about.png" alt="About Page"/>
      <p align="center"><b>About Us Page</b></p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <img src="https://raw.githubusercontent.com/rehansheikhcareer1/Business-Website/main/screenshots/login.png" alt="Login"/>
      <p align="center"><b>Secure Login</b></p>
    </td>
    <td width="50%">
      <img src="https://raw.githubusercontent.com/rehansheikhcareer1/Business-Website/main/screenshots/signup.png" alt="Signup"/>
      <p align="center"><b>User Registration</b></p>
    </td>
  </tr>
</table>

</div>

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [API Endpoints](#-api-endpoints)
- [Screenshots](#-screenshots)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

---

## ✨ Features

<div align="center">

### 💼 Complete Business Solution in One Package

*Everything you need to establish a professional online presence*

</div>

### 🎯 Core Functionality

#### **Service Management System**
- ✅ Dynamic service catalog with CRUD operations
- ✅ Service detail pages with rich descriptions
- ✅ Image upload support for service showcase
- ✅ Pricing display and management
- ✅ Active/Inactive service toggle
- ✅ Related services recommendations
- ✅ Automatic short description generation

#### **Contact Management**
- ✅ Professional contact form with validation
- ✅ Email notifications to admin on new submissions
- ✅ Contact message storage in database
- ✅ Read/Unread status tracking
- ✅ Phone number support (optional field)
- ✅ Subject categorization
- ✅ Admin panel for message management

#### **User Authentication & Authorization**
- ✅ Secure user registration with validation
- ✅ Login/Logout functionality
- ✅ Password strength validation
- ✅ User profile management
- ✅ Protected routes with @login_required
- ✅ Session management
- ✅ Automatic login after registration
- ✅ "Next" page redirect support

#### **Admin Dashboard**
- ✅ Full Django admin interface
- ✅ Service management
- ✅ Contact message inbox
- ✅ User management
- ✅ Custom admin actions

### 🎨 Frontend Features
- Responsive design (mobile-first approach)
- Clean and modern UI
- Template inheritance for consistency
- Dynamic content rendering
- Flash messages for user feedback
- SEO-friendly structure

### 🔒 Security Features
- CSRF protection enabled
- Password hashing with Django's built-in system
- SQL injection prevention
- XSS protection
- Secure session management
- Environment variable support for sensitive data

---

## 🛠️ Tech Stack

### Backend
- **Framework**: Django 4.2.7
- **Language**: Python 3.11+
- **Database**: SQLite (Development) / MySQL (Production Ready)
- **ORM**: Django ORM

### Frontend
- **Template Engine**: Django Templates
- **Styling**: CSS3
- **JavaScript**: Vanilla JS

### Additional Libraries
- **Pillow**: Image processing and upload handling
- **python-decouple**: Environment variable management
- **Django Email Backend**: SMTP email integration

---

## 📁 Project Structure

```
business-website/
│
├── business_site/              # Main project configuration
│   ├── __init__.py
│   ├── settings.py            # Project settings
│   ├── urls.py                # Root URL configuration
│   ├── views.py               # Homepage and about views
│   ├── wsgi.py                # WSGI configuration
│   └── asgi.py                # ASGI configuration
│
├── services/                   # Services app
│   ├── models.py              # Service model
│   ├── views.py               # Service views
│   ├── urls.py                # Service URLs
│   ├── admin.py               # Admin configuration
│   └── migrations/            # Database migrations
│
├── contact/                    # Contact form app
│   ├── models.py              # ContactMessage model
│   ├── views.py               # Contact form handling
│   ├── forms.py               # Contact form validation
│   ├── urls.py                # Contact URLs
│   └── admin.py               # Admin configuration
│
├── accounts/                   # User authentication app
│   ├── views.py               # Auth views (login, signup, logout)
│   ├── forms.py               # Auth forms
│   ├── urls.py                # Auth URLs
│   └── admin.py               # User admin
│
├── templates/                  # HTML templates
│   ├── base.html              # Base template
│   ├── home.html              # Homepage
│   ├── about.html             # About page
│   ├── accounts/              # Auth templates
│   │   ├── login.html
│   │   ├── signup.html
│   │   └── profile.html
│   ├── services/              # Service templates
│   │   ├── service_list.html
│   │   └── service_detail.html
│   └── contact/               # Contact templates
│       └── contact.html
│
├── static/                     # Static files
│   ├── images/                # Images and logos
│   ├── css/                   # Stylesheets
│   └── js/                    # JavaScript files
│
├── media/                      # User uploaded files
│   └── services/              # Service images
│
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

---

## 🚀 Installation

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Git
- Virtual environment (recommended)

### Step-by-Step Setup

1. **Clone the repository**
```bash
git clone https://github.com/rehansheikhcareer1/business-website.git
cd business-website
```

2. **Create and activate virtual environment**

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

5. **Run database migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create superuser (admin account)**
```bash
python manage.py createsuperuser
```

7. **Collect static files**
```bash
python manage.py collectstatic
```

8. **Run development server**
```bash
python manage.py runserver
```

9. **Access the application**
- Website: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/

---

## ⚙️ Configuration

### Email Configuration

For Gmail SMTP (recommended for development):

1. Enable 2-Factor Authentication on your Gmail account
2. Generate an App Password: https://myaccount.google.com/apppasswords
3. Update `settings.py` or `.env`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-16-digit-app-password'
```

### Database Configuration

**Development (SQLite - Default):**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

**Production (MySQL):**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'business_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Security Settings for Production

Update `settings.py`:
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECRET_KEY = os.environ.get('SECRET_KEY')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

---

## 📖 Usage

### Admin Panel

1. Login to admin panel: http://127.0.0.1:8000/admin/
2. **Manage Services:**
   - Add new services with title, description, image, and price
   - Toggle service active/inactive status
   - Edit or delete existing services

3. **View Contact Messages:**
   - Check all customer inquiries
   - Mark messages as read
   - Respond to customer queries

4. **Manage Users:**
   - View registered users
   - Modify user permissions
   - Deactivate accounts if needed

### User Features

**For Visitors:**
- Browse services on homepage
- View detailed service information
- Submit contact form inquiries
- Register for an account

**For Registered Users:**
- Login to access profile
- View personalized content
- Manage account settings

---

## 🔌 API Endpoints

### Public Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Homepage with featured services |
| GET | `/about/` | About us page |
| GET | `/services/` | List all active services |
| GET | `/services/<id>/` | Service detail page |
| GET/POST | `/contact/` | Contact form |

### Authentication Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/accounts/signup/` | User registration |
| GET/POST | `/accounts/login/` | User login |
| GET | `/accounts/logout/` | User logout |
| GET | `/accounts/profile/` | User profile (protected) |

### Admin Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/admin/` | Django admin panel |

---

## 📸 Screenshots

### 🏠 Homepage - Welcome to BusinessPro
<div align="center">
  <img src="https://raw.githubusercontent.com/rehansheikhcareer1/Business-Website/main/screenshots/home.png" alt="Homepage" width="800"/>
  
  **Modern landing page with gradient design featuring:**
  - Hero section with call-to-action
  - Services showcase section
  - Client testimonials with 5-star ratings
  - Responsive navigation with mobile menu
  - Professional footer with quick links
</div>

---

### 📖 About Us - Company Information
<div align="center">
  <img src="https://raw.githubusercontent.com/rehansheikhcareer1/Business-Website/main/screenshots/about.png" alt="About Page" width="800"/>
  
  **Comprehensive about page displaying:**
  - Company statistics (500+ Clients, 50+ Team Members, 1000+ Projects, 5+ Years Experience)
  - Mission, Vision, and Values
  - Why Choose Us section with key benefits
  - Expert team, Custom solutions, Proven results
  - 24/7 Support and Best value propositions
</div>

---

### 🔐 User Authentication System

<div align="center">
  
#### Login Page
<img src="https://raw.githubusercontent.com/rehansheikhcareer1/Business-Website/main/screenshots/login.png" alt="Login Page" width="700"/>

**Secure login interface with:**
- Clean gradient design (Purple to Orange)
- Username and password fields
- "Welcome Back" greeting
- Sign up link for new users
- Session management

---

#### Sign Up Page
<img src="https://raw.githubusercontent.com/rehansheikhcareer1/Business-Website/main/screenshots/signup.png" alt="Signup Page" width="700"/>

**User registration form featuring:**
- First Name & Last Name fields
- Username with validation
- Email address verification
- Password with confirmation
- "Join BusinessPro" branding
- Secure account creation

</div>

---

### ✨ Key UI Features

| Feature | Description |
|---------|-------------|
| 🎨 **Modern Design** | Beautiful gradient color scheme (Purple → Red → Orange) |
| 📱 **Responsive Layout** | Mobile-first design that works on all devices |
| 🔒 **Secure Forms** | Input validation and CSRF protection |
| ⭐ **Client Reviews** | 5-star rating system with testimonials |
| 📊 **Statistics Display** | Real-time business metrics showcase |
| 🎯 **Clear CTAs** | Strategic call-to-action buttons throughout |

---

## 🌐 Deployment

### Deploy to PythonAnywhere

1. **Create PythonAnywhere account**
   - Sign up at https://www.pythonanywhere.com

2. **Upload your code**
```bash
git clone https://github.com/rehansheikhcareer1/business-website.git
```

3. **Create virtual environment**
```bash
mkvirtualenv --python=/usr/bin/python3.11 myenv
pip install -r requirements.txt
```

4. **Configure WSGI file**
   - Update `/var/www/yourusername_pythonanywhere_com_wsgi.py`

5. **Set environment variables**
   - Add in PythonAnywhere web tab

6. **Collect static files**
```bash
python manage.py collectstatic
```

7. **Reload web app**

### Deploy to Heroku

1. **Install Heroku CLI**
2. **Create Heroku app**
```bash
heroku create your-app-name
```

3. **Add Procfile**
```
web: gunicorn business_site.wsgi
```

4. **Install gunicorn**
```bash
pip install gunicorn
pip freeze > requirements.txt
```

5. **Deploy**
```bash
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
```bash
git checkout -b feature/AmazingFeature
```

3. **Commit your changes**
```bash
git commit -m 'Add some AmazingFeature'
```

4. **Push to the branch**
```bash
git push origin feature/AmazingFeature
```

5. **Open a Pull Request**

### Coding Standards
- Follow PEP 8 style guide
- Write meaningful commit messages
- Add comments for complex logic
- Update documentation for new features

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Developer

**Rehan Sheikh**
- GitHub: [@rehansheikhcareer1](https://github.com/rehansheikhcareer1)
- Email: rehan.sheikh.career1@gmail.com

---

## 📞 Contact & Support

For questions, suggestions, or support:

- **Email**: rehan.sheikh.career1@gmail.com
- **GitHub Issues**: [Create an issue](https://github.com/rehansheikhcareer1/business-website/issues)
- **LinkedIn**: [Connect with me](https://linkedin.com/in/rehansheikhcareer1)

---

## 🙏 Acknowledgments

- Django Documentation
- Python Community
- Bootstrap for UI inspiration
- All contributors and supporters

---

## 📊 Project Stats

- **Lines of Code**: 2000+
- **Models**: 2 (Service, ContactMessage)
- **Views**: 8+
- **Templates**: 10+
- **Apps**: 3 (services, contact, accounts)

---

## 🔄 Version History

### v1.0.0 (Current)
- ✅ Initial release
- ✅ Service management system
- ✅ Contact form with email notifications
- ✅ User authentication
- ✅ Admin dashboard
- ✅ Responsive design

### Upcoming Features (v1.1.0)
- 🔜 Blog section
- 🔜 Newsletter subscription
- 🔜 Social media integration
- 🔜 Advanced search functionality
- 🔜 Service categories
- 🔜 Customer testimonials
- 🔜 Multi-language support

---

## 💡 Tips & Best Practices

1. **Security**: Always use environment variables for sensitive data
2. **Performance**: Enable caching for production
3. **Backup**: Regular database backups recommended
4. **Updates**: Keep Django and dependencies updated
5. **Testing**: Write tests for critical functionality

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

Made with ❤️ by [Rehan Sheikh](https://github.com/rehansheikhcareer1)

</div>
