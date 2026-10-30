# SQL Design Document
---

## Overview

This document describes the database schema, table relationships, data access methods, and tests for the Penny expense tracker application. This serves as a design document that defines how the data is stored, accessed, and validated.
The backend uses SQLite via Flask SQL Alchemy.

---

# Database Tables

This appplication requires, at a minimum, the following tables:  

## 1) Table: users  

### Table Description  
Stores user account information for Penny users.  

### Fields

| Field Name | Description | Constraints |
|------|------|-----|
| id | Unique ID assigned to each registered user | Non-nullable primary key|
| username | Unique username for each registered user | Non-nullable, unique |
| first_name | Registered user's first name |Non-nullable |
| last_name | Registered user's last name | Non-nullable |
| email | Registered user's unique e-mail | Non-nullable, unique|g
| password_hash | Hashed value of registered user's password | Non-nullable|
| creation_time | Time of registered user's account creation | Non-nullable|

### Relationships

- One-to-many with `expense_trans`
- One-to-many with `expense_cats`

### Table Tests
**Use Case:** Creating a user record  
**Description:** Simulate a user registering an account and confirm that the record of their information exists  
**Pre-conditions:** App and DB are up and running  

**Test Steps:**  
1) Fill out registration form, submitting a valid row of user data  
2) Query the DB for that row using the email you provided in step 1  
**Expected Result:** Row submitted in step 1 exists  

---

## 2) Table: expense_trans

### Fields

| Field Name | Description | Constraints |
| ----- | ----- | ----- |
| id | Unique ID assigned to each transaction added to Penny | Non-nullable primary key|
| amount | Dollar amount of expense transaction | Non-nullable |
| title | Title of expense transaction | Non-nullable|
| description | Description of expense transaction | Non-nullable |
| category_id | ID representing the category of the expense transaction | Non-nullable foreign key to `expense_cats`|
| user_id | ID associated with the user adding the expense | Non-nullable foreign key to `users` |
| expense_date | Date of expense transaction | Non-nullable |

### Relationships

- Many-to-one with `users`  
- Many-to-one with `expense_cats`  

### Table Tests

**Use Case:** Adding an expense as a user  
**Description:**  Simulate adding an expense as a registered user of the app  
**Pre-conditions:** App and DB are up and running, Registered testing account exists in the DB  

**Test Steps:**
1) Fill out all required fields for adding an expense to Penny  
2) Query the db for that record using the date and expense title provided in step 1 as well as the user ID associated w/ the test account  

**Expected Result:** Expense submitted in step 1 exists for the testing user account and is displayed when queried  
**Post-conditions:** The expense persists and is queryable in follow-on sessions  

---

## 3) Table: expense_cats

### Fields
| Field Name | Description | Constraints |
| ----- | ----- | ----- |
| id | Unique ID assigned to each expense category added to Penny | Non-nullable primary key |
| name | Expense category name | Non-nullable |
| user_id | ID associated with the user that added the expense category | Nullable foreign key to `users` |

### Relationships

- Many-to-one with `users`  
- One-to-many with `expense_trans`  

### Table Tests

**Use Case:** Creating an expense category as a user   
**Description:** Simulate adding an expense category as a registered user of the app  
**Pre-conditions:** App and DB are up and running, Registered testing account exists in the DB  

**Test Steps:**
1) Fill out all required fields for adding an expense category to Penny  
2) Query the DB for the category created in step 1 using the category name and user ID associated w/ the test account  

**Expected Results:** The expense category created in step 1 exists in the DB and is displayed when queried  
**Post-conditions:** The expense category persists and is queryable and usable in follow-on sessions  

---

# Data Access Methods

## get_user_by_username()

**Description:** Query DB for a user record using a username as the parameter  
**Parameters:** username (string)  
**Return Values:** User record linked to username or NULL  

**Tests:**  
1) Pass a known, registered username to the method and ensure that it returns a user record  
2) Pass a known, available, unregistered username to the method and ensure that it returns NULL  

---

## get_user_transactions()

**Description:** Query DB for all expense records that a user has entered  
**Parameters:** user_id (int)  
**Return Values:** All expense records tied to user or NULL  

**Tests:**  
1) Pass a known, registered user_id with existing records to the method and ensure that it returns all related records  
2) Pass a known, available, unregistered, user id to the method and ensure that it returns NULL  

---

## get_user_categories()

**Description:** Query DB for all expense categories available to a user  
**Parameters:** user_id (int)  
**Return Values:** Base categories provided by Penny or base categories + user's custom categories  

__Tests:__  
1) Pass a known, registered user id with existing custom categories to the method and ensure that it returns the base set of categories + any custom user defined categories  
2) Pass a known, available, unregistered user id to the method and ensure that it returns the base set of categories  
