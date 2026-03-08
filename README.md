# Unsecure_Login-system - Student Instructions

This project is a deliberately insecure Flask login demo for security analysis.

Your task is to run the application in **GitHub Codespaces**, test it, inspect the code, and identify security weaknesses.

---

## Project Purpose

This application is intentionally insecure so students can investigate common web security issues.

---

## Files in This Project

- `app.py` → Flask application
- `schema.sql` → database structure and sample user data
- `requirements.txt` → Python packages required
- `templates/login.html` → login page
- `templates/result.html` → result page

---

## How to Run the Project in GitHub Codespaces

### Step 1 – Open the Repository
Open the GitHub repository provided by your teacher.

---
### Step 2 – Create a Codespace
1. Click the **Code** button
2. Click the **Codespaces** tab
3. Click **Create codespace on main**

GitHub will open a VS Code environment in your browser.

---

### Step 3 – Wait for Codespaces to Load
Wait until the editor and terminal finish loading.

---

### Step 4 – Open a Terminal
If the terminal is not already open:

1. Click **Terminal**
2. Click **New Terminal**

---

### Step 5 – Install the Required Package
Run this command in the terminal:

```bash
pip install -r requirements.txt

---

# Step 6 – Run the Application

Run the following command:

python app.py

You should see a message indicating the Flask server is running.
This installs the Flask framework required for the application.
---

# Step 7 – Open the Web Application

GitHub Codespaces will detect the running server.

1. Look for the **Ports** tab at the bottom.
2. Find **Port 5000**.
3. Click **Open in Browser**.

The login page should appear.

---

# Step 8 – Test the Login System

Try logging in with the following test accounts:

Username: teacher
Password: password123

Username: student
Password: abc123

Username: admin
Password: admin

---

# Step 9 – Investigate the Application

Inspect the following files:

* app.py
* schema.sql
* templates/login.html
* templates/result.html

Also examine the database file created when the program runs.

---

# Step 10 – Identify Security Vulnerabilities

---

# Step 11 – Document Your Findings

For each vulnerability you discover, record:

1. The vulnerability name
2. Evidence from the code or application
3. Why it is a security risk
4. A recommended fix

---

# Troubleshooting

If the application does not run:

### Flask not installed

Run:

pip install -r requirements.txt

### Port not opening

Check the **Ports** panel and manually open **Port 5000**.

### Database error

Delete the file:

users.db

Then run:

python app.py

The database will be recreated automatically.

---

# Important

This application is intentionally insecure and is used only for educational analysis.

Do not deploy this application on a public server.
