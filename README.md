
# 🛍️ E-Project – Full-Stack E-commerce Platform for a Stationery Shop

Welcome to **Craft Studio**, a feature-rich e-commerce web application tailored for a stationery shop. This full-stack project offers a complete online shopping experience with user authentication, product browsing, cart management, and order placement. Built using **Django** and **MySQL**, with a responsive UI powered by **Bootstrap 5**, Craft Studio is ideal for modern web commerce.

---

## 🔍 Project Overview

Craft Studio enables customers to:

- Browse category-based stationery products
- Add/remove items to a shopping cart
- Register and manage user accounts securely
- Place orders with preferred payment methods (Cash on Delivery/UPI)
- View past order history
- Shop from any device with a mobile-friendly UI

---

## 🚀 Key Features

### 🔐 User Authentication
- Sign up, log in, and log out
- Secure session handling
- Access control for shopping features

### 📦 Dynamic Product Listing
- Browse items by category (Pens, Notebooks, Art Supplies)
- Filtered and organized product views

### 🛒 Shopping Cart System
- Add/remove products from cart
- Quantity adjustment and real-time totals
- Clean and simple cart UI

### 📤 Order Placement
- Confirm and place orders securely
- Payment options: Cash on Delivery / UPI
- Success confirmation page

### 📋 Order History
- View list of previous orders
- Track item names, dates, and statuses

### 📱 Responsive UI
- Built with **Bootstrap 5**
- Mobile-first design with custom CSS enhancements

---

## 🛠️ Tech Stack

| Layer        | Technology               |
|--------------|--------------------------|
| Backend      | Django (Python)          |
| Database     | MySQL                    |
| Frontend     | HTML5, CSS3, Bootstrap 5 |
| Templating   | Django Templates (Jinja2)|
| Version Control | Git, GitHub           |


---

## ⚙️ How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ron0011/E-Commerce-.git
   cd Craft-Studio/codealpha_project
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MySQL database**
   - Create a new MySQL database (e.g., `craftstudio_db`)
   - Update database settings in `settings.py`

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the app**
   Open browser and go to: [http://localhost:8000](http://localhost:8000)

---

## 📁 Folder Structure

```
Craft-Studio/
│
├── codealpha_project/
│   ├── ecommerce/
│   │   ├── templates/
│   │   │   └── ecommerce/
│   │   ├── static/
│   │   ├── views.py
│   │   ├── models.py
│   │   └── urls.py
│   ├── manage.py
│   └── db.sqlite3 (or MySQL DB connection)
│
├── README.md
└── requirements.txt
```

---

