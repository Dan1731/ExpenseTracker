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
**Week:** 9 <br>
**Meeting Held:** No <br>
**Date:** November 23, 2026 <br>
Team opted not to meet during Thanksgiving Break but communicated updates via Email. <br>

## Progress Since Last Week
 
There was no meeting this week, but work on the dashboard and the expense table continued:
 
- **Dashboard data:** Miles pushed the SQL that groups and queries spending data for the dashboard. It has one small error, which he plans to fix.
- **Dashboard charts:** Miles built first-draft Plotly charts on a "Spending Dashboard" page: a bar chart and a pie chart of expenses by category. The page also has a placeholder filter bar for Start Date, End Date, Lower Amount and Upper Amount. He will keep refining the charts this week.
- **Dashboard page:** Layce created and routed an empty dashboard page in the app. Plotly's fig.to_html(full_html=False) returns just the chart's <div>, which can be dropped into the template like any other variable.
- **Expense Table:** Claudia finished the Expense Table. It shows summary cards (Total Expenses, Transactions, Largest Expense), search by title, a category filter and start/end date filters. Each row has an actions menu for Edit, Delete and Copy.
- **Edit Expense:** Edit reuses the Add Expense page as an "Edit Expense" form with the fields filled in and a link back to the Expense Table.
- **Unit tests:** Layce wrote unit tests for the profile page and for logging out.
  
---
 
## Completed Tasks
 
- First-draft Plotly visualizations: bar and pie charts of expenses by category
- Empty dashboard page created and routed
- Expense Table summary cards, search and filters
- Expense Table row actions: Edit, Delete, Copy
- Unit tests for logout and the profile page

---
 
## Planned Tasks for Next Week
- Fix the small error in the dashboard SQL
- Polish the Plotly charts and connect the filter bar (date range and amount range)
- Put the Plotly charts into the dashboard page
- Draft the final presentation--each member adds slides for their part of the demo

---
 
## Blockers and Issues
- No meeting this week. The meeting slipped everyone's mind over the holiday, so updates came in by email instead. The team hasn't discussed the next steps together yet.
- Dashboard SQL error (still open). Miles pushed the SQL with a small error and said he'd fix it.
- Unit tests not on main yet. Layce's logout and profile tests are written but haven't been pushed. Logout stays out of Done until they are.

---
 
## Risks and Mitigation
- Per-user data on the dashboard. A Plotly chart exported once as a static HTML file would always show the same data and wouldn't respond to filters. The dashboard has to show only the logged-in user's expenses. Mitigation: build the charts in the Flask route on each request using the session's user, either as embedded HTML or as JSON (embedded HTML seems the better option for this project).
- Less time before the demo. The holiday cut into coordination near the end of the semester. Mitigation: the team kept sending updates by email, and Miles is starting the presentation draft early.
- Chart readability. Very small categories, like Food and Phone, show as tiny slices on the pie chart with crowded labels. Mitigation: Miles is polishing the charts this week. Options include grouping small categories or leaning on the bar chart.

## Individual Contributions This Week
- **Layce Smith:**
  - Wrote unit tests for the profile page and for logging out of a user session. Will push them to main.
  - Created and routed an empty dashboard page to hold the Plotly charts.
  - Documented email chain lieu of a zoom call 
- **Miles Devine:**
  - Pushed the dashboard SQL for grouping and querying spending data. Fixing a small error in it.
  - Built first-draft Plotly charts (bar and pie charts of expenses by category) and a placeholder filter bar.
  - Next week: polish the visualizations and draft the PowerPoint for the final demo.
- **Claudia Vargas:**
  - Finished the Expense Table, including summary cards, search, category and date filters.
  - Added the row actions menu (Edit, Delete, Copy).
  - Built Edit Expense by reusing the Add Expense page.

---

## Reporting Period
**Week:** 8 <br>
**Meeting Held:** Yes <br>
**Meeting Date:** November 16, 2026 <br>
**Meeting Duration:** 20 minutes <br>
**Meeting Format:** Zoom <br>
**Meeting Recording:** (https://o365coloradoedu-my.sharepoint.com/personal/mide6922_colorado_edu/_layouts/15/stream.aspx?id=%2Fpersonal%2Fmide6922%5Fcolorado%5Fedu%2FDocuments%2FAttachments%2Fvideo1588372712%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E33e1f0d3%2D579a%2D427e%2Dac91%2Df7e3cdb5c9e9)

---

## Progress Since Last Week

Since the last meeting, the app's pages are connected and users can move through it end to end:

- **User sessions and data isolation:** Queries now use the session variable. Users see only the categories they created, and each transaction they post is tied to the logged-in user. The session check lives in the app file, so any route can send a logged-out user back to the login page.
- **Page navigation:** The side navigation panel now links every page except the dashboard. Logout ends the session and returns the user to the sign-in page.
- **Add Expense page fixes:** The side panel was cut off on the Add Expense page in smaller windows. Miles adjusted the page, and it displayed correctly by the end of the meeting. A build error came up when clicking "Add Expense" while not signed in. The redirect path to the login page needs updating.
- **Custom categories:** The team agreed to add an "Add Category" button on the right side of the Add Expense page. It will open a page where users can add categories and then send them back to Add Expense. This work is in progress on a local branch.
- **Dashboard research:** The team ruled out Tableau, because its dashboards are built around a shared dataset and can't easily limit each user to their own data. The dashboard will use a Flask route that returns JSON, with Plotly for the charts. Chart.js and Jinja templates are the backups.
- **Trello cleanup:** The team reviewed the board and moved finished items to Done.

---

## Completed Tasks

- User session handling, including per-user data isolation for categories and transactions
- Logout and session end (marked done pending unit tests)
- Login validation
- Page navigation between pages via the side panel
- Keeping entered values on the Add Expense form when a submission has an error
- Researched dashboard options and chose Flask JSON + Plotly
- Unit tests for the expense table and login

---

## Planned Tasks for Next Week
- Fix the Add Expense redirect path for users who aren't signed in
- Finish the "Add Category" button and page
- Write unit tests for logout
- Finish the filtering logic on the Expense Table
- Dashboard: write the SQL to group and query the data
- Dashboard: build the Flask JSON route and Plotly charts
- Split the dashboard work into front-end and back-end tasks and assign them
- Link the dashboard in the navigation panel

---

## Blockers and Issues
- Add Expense build error (still open). Claudia got a build error when she opened Add Expense without being signed in. The route checks the session but doesn't send the user to the login page correctly. It's probably a path fix, and Miles said he'd update it.
- Side panel cut off on Add Expense (fixed). Layce saw the navigation panel cut off in a small window. By the end of the meeting the page looked fine after Miles's changes.
- Logout can't be marked done yet. It works and Layce tested it by hand, but there are no unit tests. Layce will write them before moving the card to Done.

---

## Risks and Mitigation
- Unclear testing expectations. The team wasn't sure how much unit testing the professor expects. Claudia thought test cases are needed for the final report. The team decided to write unit tests for finished features, starting with logout.
- Nobody has used Plotly yet. Layce hasn't tried it and will look into it more. Chart.js and Jinja templates are the backups if Plotly doesn't work out.
- Where the session check lives. Layce put it in the app file instead of Claudia's login file and offered to move it if anyone objected. Miles said it works well because it can protect every route, so no change is needed.

## Individual Contributions This Week

- **Layce Smith:**
  - Added the user session variable--put the session check in the app file rather than in Claudia's login file.
  - Added links for every page to the side navigation panel. Only the dashboard is still missing.
  - Made logout work: it ends the session and returns to the sign-in page. (Will write unit tests before marking it done.)
  - Found that the side panel was cut off on the Add Expense page.
  - Researched dashboard options and recommended Flask JSON with Plotly over Tableau.
  
- **Miles Devine:**
  - Used the session variable in his queries, so users see only their own categories and their transactions belong to them. He pushed this to main.
  - Owns the Add Expense page and adjusted its layout for the side panel.
  - Building the "Add Category" button and page on a local branch.
  - Will fix the login redirect path on the Add Expense route.
  - Ran the meeting and is sending out the recording.
  - Next week: write the SQL that groups and queries the data for the dashboard.
  
- **Claudia Vargas:**
  - Found the build error that happens when you open Add Expense without being signed in.
  - Login validation.
  - Made the Add Expense form keep entered values when a submission has an error.
  - Wrote unit tests for the expense table and for login.
  - Added items to the Trello board and led most of the cleanup.
  - Next week: finish the filtering logic on the expense table, then help with the dashboard.

---

## Reporting Period
**Week:** 7 <br>
**Meeting Held:** Yes <br>
**Meeting Date:** November 9, 2026 <br>
**Meeting Duration:** 30 minutes <br>
**Meeting Format:** Zoom (not recorded) <br>

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
Work on remaining backlog items:
- User Session
- Data isolation for multi users
- Add page navigation between pages
- Unit Testing for math logic
- Determine task priorities for the upcoming week and divvy up the work

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
Work on remaining backlog items:
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

---

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
Work on remaining backlog items:
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

---

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


