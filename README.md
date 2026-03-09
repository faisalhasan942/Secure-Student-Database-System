# Secure Student Database Management System

## Project Overview

The Secure Student Database Management System is a mini project developed using Python (Jupyter Notebook) and MySQL to demonstrate important database security concepts.

The system securely manages student records and implements multiple security mechanisms such as password hashing, SQL injection prevention, role-based access control, and audit logging.

The project demonstrates how sensitive data stored in databases can be protected from unauthorized access and common cyber attacks.

---

## Objectives

* Implement secure database authentication.
* Prevent SQL injection attacks.
* Enforce role-based access control (RBAC).
* Track user activities using audit logs.
* Protect user credentials using cryptographic hashing.

---

## Technologies Used

| Technology             | Purpose                |
| ---------------------- | ---------------------- |
| Python                 | Backend logic          |
| Jupyter Notebook       | Project implementation |
| MySQL                  | Database management    |
| bcrypt                 | Password hashing       |
| mysql-connector-python | Database connection    |

---

## Database Structure

The project uses three main tables.

### Users Table

Stores login credentials and security information.

Fields:

* user_id (Primary Key)
* username
* password_hash
* role
* failed_attempts
* account_locked
* created_at

### Students Table

Stores student information.

Fields:

* student_id (Primary Key)
* name
* phone
* address
* marks
* created_at

### Logs Table

Stores activity records for auditing purposes.

Fields:

* log_id
* user_id
* action
* timestamp

---

## Security Features Implemented

### Password Hashing

Passwords are hashed using bcrypt before storing in the database. This ensures that plain-text passwords are never stored.

### SQL Injection Prevention

The system uses parameterized queries (prepared statements) to ensure user inputs cannot modify SQL queries.

Example:

```
cursor.execute(query, (username,))
```

### Role-Based Access Control

Users are assigned specific roles such as Admin, Teacher, and Student. Access to certain operations is restricted based on the role.

### Account Lock Mechanism

If a user enters the wrong password three times, the account is automatically locked to prevent brute force attacks.

### Audit Logging

All important system activities are recorded in the logs table, including login attempts and data modifications. This helps monitor suspicious behavior.

---

## System Workflow

1. A user registers with a username and password.
2. The password is hashed using bcrypt before being stored in the database.
3. The user logs into the system using secure authentication.
4. The system verifies the user role.
5. Admin users can add student records to the database.
6. Every action performed in the system is recorded in the logs table.

---

## Running the Project

### Step 1

Install the required Python libraries:

```
pip install mysql-connector-python bcrypt
```

### Step 2

Create the database using MySQL Workbench.

### Step 3

Run the SQL queries to create the required tables.

### Step 4

Open the project in Jupyter Notebook.

### Step 5

Run the notebook cells sequentially to execute the system.

---

## Security Concepts Demonstrated

* Authentication
* Authorization
* Password hashing
* SQL injection prevention
* Brute force protection
* Audit logging
* Data integrity constraints

---

## Future Improvements

* Encrypt sensitive student data
* Implement a graphical user interface using Flask
* Add multi-factor authentication
* Implement CAPTCHA protection
* Extend the logging system for intrusion detection

---

## Author

Faisal Hasan
B.Tech Computer Science Engineering (Cyber Security)

---

## License

This project is developed for educational and academic purposes.
