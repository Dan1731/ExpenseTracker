## Weekly Status Report

**Project:** Penny (Expense Tracker)
**Team Number:** 1
**Team Name:** Penny

---

## Overview

The **Penny** expense tracking project is a collaborative effort between Claudia Vargas, Layce Smith, and Miles Devine. The goal of the project is for the team to meet and work together using an Agile methodology so that
each member understands the road map and what is expected of them as individual contributors of the web application in development. 

This particular document is a log of each week of the project, with the most recent week at the top.

---

## Project Management Snapshot

The team is using a shared **Trello board** to manage tasks and sprint progress.
At the time of this report:
- Columns include: Backlog, In Progress, In Review, Done
- Tags include: Discovery, Scoping, Frontend, and Backend
- Tasks are claimed by individual team members.
- Tasks are arranged by row in order of priority.
- Due dates are set by team members working on given tasks.
- **Link:** https://trello.com/invite/b/6abb0873fbed94233b84b519/ATTI9d9ae8209ba5744a7ee7c92fb494583e1BC045CB/expensetracker3308project

---

## Reporting Period
**Week:** 6 <br>
**Meeting Held:** Yes <br>
**Meeting Date:** November 2, 2026 <br>
**Meeting Duration:** 26 minutes <br>
**Meeting Format:** Zoom <br>
**Meeting Recording:** https://app.clipchamp.com/consumer/login?driveId=FDC8FF5722947CCB&folderId=FDC8FF5722947CCB%21s2a3a009049dd4ce7a918fefaae62d334&itemId=FDC8FF5722947CCB%21s0a79b417e9714203a4d8fe78bc385e0e

---

## Progress Since Last Week

This week, the team meeting was focused on updating the backlog to get a better sense of what still needs to be done. 

## Completed Tasks

This week, the team completed the following items from the backlog: 
- Design Add Expense Form
- Create Predefined Categories
- Expense Table Page

---

## Planned Tasks for Next Week
Work on backlog items:
- User Session
- Data isolation for multi users
- Add page navigation between pages
- Unit Testing for math logic
- Determine task priorities for the upcoming week and divvy up the work

---

---

## Reporting Period
**Week:** 5 <br>
**Meeting Held:** Yes <br>
**Meeting Date:** October 26, 2026 <br>
**Meeting Duration:** 26 minutes <br>
**Meeting Format:** Zoom <br>
**Meeting Recording:** https://o365coloradoedu-my.sharepoint.com/:v:/g/personal/mide6922_colorado_edu/IQDLAFmBqKFGSL_1nY4kllAtAZPu7p7d0bNXeaU1RBf1pcM?e=Xb9am8&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D

---

## Progress Since Last Week
 
Last week, the team reviewed the page specifications in `PAGE_TESTING.md`, and Miles demoed the Flask-SQLAlchemy/SQLite database and the `seed_db.py` script that generates fake test data.
 
This week, the team demoed working pages running locally on the Flask app:
 
- **User Profile page (Layce):** On the `UserProfile` branch, Layce added a `profile_route.py` Flask Blueprint with a `/profile/<username>` route. It looks up the user in the database, returns a 404 if the user doesn't exist, and renders `profile.html`, styled by a new `profile.css`. The page shows the user's username and avatar, editable first name, last name and email fields, a "Save changes" button, and a "Back to dashboard" link.
- **Add Expense page (Miles):** Miles demoed the `/add_expense` page. It is a form with Title, Description, Amount, Category (dropdown) and Date fields, an "Add Expense" button, and a "Back to Expense Table" link.

---

## Completed Tasks
 
- Built the User Profile page: the `profile_route.py` Blueprint, `profile.html` and `profile.css`
- Added a 404 response for profile URLs whose username doesn't exist
- Built the Add Expense form page and its `/add_expense` route

---

## Planned Tasks for Next Week
Work on backlog items:
- Login Validation
- Account Registration Validation
- User Session
- Design Add Expense Form
- Create Predefined Categories
- Data isolation for multi users
- Add page navigation between pages
- Report/Graphs for Dashboard
- Expense Table Page
- Unit Testing for math logic
- Determine task priorities for the upcoming week and divvy up the work

---

## Individual Contributions This Week
 
- **Layce Smith:** built the User Profile page (`profile_route.py` Blueprint, `profile.html`, `profile.css`) on the `UserProfile` branch, and demoed it to the team
- **Miles Devine:** built and demoed the Add Expense form page (`/add_expense`)
- **Claudia Vargas:** documented meeting for notes

## Reporting Period
**Week:** 4 <br>
**Meeting Held:** Yes <br>
**Meeting Date:** October 19, 2026 <br>
**Meeting Duration:** 25 minutes <br>
**Meeting Format:** Zoom <br>
**Meeting Recording:** https://o365coloradoedu-my.sharepoint.com/personal/mide6922_colorado_edu/_layouts/15/stream.aspx?id=%2Fpersonal%2Fmide6922%5Fcolorado%5Fedu%2FDocuments%2FAttachments%2Fvideo1273623242%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E058acfb1%2D5fb8%2D4aee%2D9179%2D3e155e4d1426&ct=1794769943107&or=OWA%2DNT%2DMail&cid=82bb350b%2D9ee9%2D3b2a%2Dda38%2D8989309e1fb2&ga=1&LOF=1

---

## Progress Since Last Week

Last week, the team discussed database design and chose SQLite, with Miles continuing on the database, Claudia on the frontend, and Layce taking on more of the backend.

This week, the team reviewed the page specifications in PAGE_TESTING.md. For each page, the spec covers the description, parameters, data needed to render, link destinations, rendering tests, and an ASCII mockup. Pages covered include the Sign In/Sign Up page, the Dashboard (four graph panels with category and date filters), and the Add Expenses pop-up form.

Miles then demoed the database work on the db_creation branch. The backend now uses Flask with Flask-SQLAlchemy on a SQLite database (expense_tracker.db), with models defined in models.py. A new seed_db.py script uses Faker to drop and rebuild the tables and generate test data: 50 users, 7 base expense categories (Housing, Groceries, Eating Out, Gas, Utilities, Healthcare, Insurance), and 5 transactions per category for each user. The team ran the script and checked the output of a query that averages each user's spending per category.

Finally, the team walked through the Trello board to review task status.

---

## Completed Tasks
- Drafted page specifications and mockups in PAGE_TESTING.md (Sign In/Sign Up, Dashboard, Add Expenses, and others)
- Completed SignIn/SignUp .html files
- Completed Account Registration Form .css
- Completed Account Registration Database
- Completed Design Dashboard Layout Review
- Built Flask-SQLAlchemy models and a SQLite database
- Wrote seed_db.py to generate fake test data with Faker, and verified it with a per-category average query
- Added requirements.txt and setup.sh for the project environment

---

## Planned Tasks for Next Week
- Finish Design Database (In Progress)
- Finish User Login Page (In Progress)
- Review and merge SignIn/SignUp .css files (In Review)
- Begin backlog items:
- Login Validation
- Account Registration Validation
- User Session
- Design Add Expense Form
- Create Predefined Categories
- Data isolation for multi users
- Add page navigation between pages
- Report/Graphs for Dashboard
- Expense Table Page
- Unit Testing for math logic
- Determine task priorities for the upcoming week and divvy up the work

---

## Individual Contributions This Week
**Claudia Vargas:** drafted page specifications and mockups in PAGE_TESTING.md, completed SignIn/SignUp .html files and Account Registration Form .css, submitted SignIn/SignUp .css files for review
**Miles Devine:** built the Flask-SQLAlchemy models and SQLite database, completed Account Registration Database, wrote seed_db.py to generate test data, continued work on Design Database
**Layce Smith:** documented meeting for notes


## Reporting Period
**Week:** 3 <br>
**Meeting Held:** Yes <br>
**Meeting Date:** October 12, 2026 <br>
**Meeting Duration:** 25 minutes <br>
**Meeting Format:** Zoom <br>
**Meeting Recording:** https://o365coloradoedu-my.sharepoint.com/:v:/g/personal/mide6922_colorado_edu/IQCv3b8roolORZnKbdd74CSDAS3zmNqJ3Sdwlm-7GdWncx4?e=aKzN9x&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D** 

---

## Progress Since Last Week

Last week, the team created user stories and established a shared understanding of a product MVP.
**Link:** https://github.com/Dan1731/ExpenseTracker/blob/Project-Milestone-2/UPDATE.md

This week, the team discussed database design and SQL options. SQL lite was chosen due to its simplicity and because any limitations due to its simplicity would fall outside the scope of the project MVP anyway. Miles agreed to continue working on the database design. Claudia, who has already coded some html for the sign up/login pages opted to continue working on frontend dev. Layce agreed to take on more of the backend work. The team agreed to research other tooling and infrastructure before the next meeting.

---

## Completed Tasks

- Created GitHub repository and added all team members
- Set up Trello project board with initial task breakdown
- Researched other expense trackers
- Defined MVP feature scope
- Drafted initial user stories
- Drafted initial UI in html for setup/login pages
- Drafted database design

---

## Planned Tasks for Next Week

- Continue refining database
- Create more .html and .css files for UI
- Set up Flask project environment
- Draft frontend and backend designs
- Determine what other languages/tools will be used in tech stack


## Blockers and Issues

The team needs to determine what other (if any) frontend/backend tools they plan to use and come up with a clear design.

During the discussion this week, React was mistakenly suggested as an alternative to Flask, but it was later understood that React is a frontend tool that is great for building highly interactive UIs, while Flask is a backend micro-framework. 

---

## Risks and Mitigation

It was brought up that implementing changes in SQL lite on database during unit testing can result in loss of data. The team's plan to mitigate this issue is to keep dataset small during unit testing so reentering data is not cumbersome.

---

## Team Reflection

The team agreed that Trello is a good way to keep track of tasks and agreed to keep using it as the project management tool.

---

## Individual Contributions This Week

- **Claudia Vargas:** setup Trello project board, drafted .css files for setup/login pages
- **Layce Smith:** drafted initial user stories, wrote WEEKLY_STATUS.md for project milestone 3
- **Miles Devine:** defined MVP feature scope, drafted .sql file for database design


