# 🎬 Netflix Clone — Django Project

A Netflix-inspired web application built with Django as part of a Full Stack Development course.
It features a login page and a home page displaying movies as cards with posters, titles, genres, ratings and descriptions.

---

## 📸 Features

- 🔐 Login page with username & password authentication
- 🎬 Home page displaying movies as Netflix-style cards
- 🖼️ Movie posters, title, genre, year, rating and description
- 🎨 Netflix dark theme with hover animations
- 🗄️ Django admin panel to manage movies
- 📄 Template inheritance with base theme

---

## 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| Python | Backend language |
| Django | Web framework |
| SQLite | Database |
| HTML & CSS | Frontend |
| Django Admin | Movie management |

---

## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/AthuljithS/Netflix_clone.git
cd Netflix_clone
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install django
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Admin Account)

```bash
python manage.py createsuperuser
```
Enter a username and password when prompted.

### 7. Run the Development Server

```bash
python manage.py runserver
```

### 8. Open in Browser

| URL | Page |
|---|---|
| `http://127.0.0.1:8000/` | Login Page |
| `http://127.0.0.1:8000/home/` | Home Page |
| `http://127.0.0.1:8000/admin/` | Admin Panel |

---

## 🎬 Adding Movies

1. Go to `http://127.0.0.1:8000/admin/`
2. Login with your superuser credentials
3. Click **Movies → Add Movie**
4. Fill in the details:
   - Title
   - Description
   - Genre
   - Image URL (direct image link ending in `.jpg` or `.png`)
   - Rating
   - Year
5. Click **Save**

---

## 📁 Project Structure

```
Netflix/
  ├── home/                   ← Django app
  │     ├── templates/
  │     │     └── home/
  │     │           ├── theme.html   ← base template
  │     │           ├── login.html   ← login page
  │     │           └── home.html    ← movies home page
  │     ├── models.py         ← Movie model
  │     ├── views.py          ← login & home views
  │     ├── urls.py           ← app URL patterns
  │     └── admin.py          ← admin registration
  ├── Netflix/                ← project settings
  │     ├── settings.py
  │     └── urls.py
  └── manage.py
```

---

## 👤 Author

**Athuljith S**
GitHub: https://github.com/AthuljithS

---

## 📝 License

This project is for educational purposes as part of a Full Stack Development internship course.
