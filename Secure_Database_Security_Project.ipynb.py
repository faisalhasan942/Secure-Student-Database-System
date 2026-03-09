#!/usr/bin/env python
# coding: utf-8

# In[14]:


get_ipython().system('pip install mysql-connector-python bcrypt')


# In[15]:


import mysql.connector
import bcrypt

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Fai@2003",  # Put your MySQL password
    database="secure_student_db"
)

cursor = db.cursor()
print("Database Connected Successfully")


# In[16]:


def register_user(username, password, role):
    
    # Password strength check
    if len(password) < 8:
        print("Password must be at least 8 characters long")
        return
    
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    query = """
    INSERT INTO users (username, password_hash, role)
    VALUES (%s, %s, %s)
    """
    
    try:
        cursor.execute(query, (username, hashed_pw.decode('utf-8'), role))
        db.commit()
        print("User Registered Successfully")
    except:
        print("Username already exists")


# In[17]:


register_user("admin1", "Admin@123", "admin")


# In[18]:


def login_user(username, password):
    
    query = """
    SELECT user_id, password_hash, role, failed_attempts, account_locked
    FROM users WHERE username = %s
    """
    
    cursor.execute(query, (username,))
    user = cursor.fetchone()
    
    if not user:
        print("User Not Found")
        return None, None
    
    user_id, stored_hash, role, failed_attempts, account_locked = user
    
    if account_locked:
        print("Account is Locked due to multiple failed attempts")
        return None, None
    
    if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
        
        # Reset failed attempts
        cursor.execute("UPDATE users SET failed_attempts = 0 WHERE user_id = %s", (user_id,))
        
        cursor.execute("INSERT INTO logs (user_id, action) VALUES (%s, %s)",
                       (user_id, "Login Successful"))
        db.commit()
        
        print("Login Successful")
        return user_id, role
    
    else:
        failed_attempts += 1
        
        if failed_attempts >= 3:
            cursor.execute("UPDATE users SET account_locked = TRUE WHERE user_id = %s", (user_id,))
            print("Account Locked due to 3 failed attempts")
        else:
            cursor.execute("UPDATE users SET failed_attempts = %s WHERE user_id = %s",
                           (failed_attempts, user_id))
            print("Invalid Password")
        
        db.commit()
        return None, None


# In[19]:


user_id, role = login_user("admin1", "Admin@123")


# In[20]:


def add_student(user_id, role, name, phone, address, marks):
    
    if role != "admin":
        print("Unauthorized Access! Only Admin Allowed.")
        return
    
    query = """
    INSERT INTO students (name, phone, address, marks)
    VALUES (%s, %s, %s, %s)
    """
    
    cursor.execute(query, (name, phone, address, marks))
    
    cursor.execute("INSERT INTO logs (user_id, action) VALUES (%s, %s)",
                   (user_id, "Added Student Record"))
    
    db.commit()
    print("Student Added Successfully")


# In[21]:


add_student(user_id, role, "Rahul", "9876543210", "Delhi", 85)


# In[22]:


def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

view_students()


# In[23]:


def view_logs():
    cursor.execute("SELECT * FROM logs")
    for log in cursor.fetchall():
        print(log)

view_logs()


# In[24]:


login_user("' OR '1'='1", "123")


# In[ ]:




