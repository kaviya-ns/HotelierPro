# HotelierPro

**A desktop hotel management system built with Python, Tkinter and MySQL.**

HotelierPro gives front-desk staff one place to register guests, book rooms, manage check-ins and check-outs, and maintain room details — all backed by a MySQL database.

![Python](https://img.shields.io/badge/Python-3670A0?logo=python&logoColor=ffdd54) ![Tkinter](https://img.shields.io/badge/GUI-Tkinter-blue) ![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white)

---

## Features

- **Staff login** screen
- **Customer management** — add, update, delete, search and list guest records (auto-generated reference numbers)
- **Room booking** — check-in / check-out dates, room type, meal plan, and automatic bill calculation
- **Room details** — maintain floors, room numbers and room types
- Clean dashboard with image banners and navigation between modules

## Modules

| File | Purpose |
|---|---|
| `login.py` | Login window — **entry point** |
| `hotel.py` | Main dashboard and navigation |
| `customer.py` | Customer CRUD |
| `room.py` | Room booking and billing |
| `details.py` | Room master data |

## Getting Started

**Prerequisites:** Python 3.8+, MySQL Server.

1. Install dependencies:
   ```bash
   pip install mysql-connector-python pillow
   ```
2. Create the database and tables in MySQL:
   ```sql
   CREATE DATABASE dbmspackage;
   ```
   Then create the `customer`, `room` and `details` tables used by the modules.
3. Update the MySQL connection settings (`host`, `user`, `password`, `database`) in the `mysql.connector.connect(...)` calls to match your local server.
4. Run:
   ```bash
   python login.py
   ```

---

*Built as the RDBMS course package project.*
