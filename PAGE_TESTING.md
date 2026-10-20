# Page Title #1:
## Sign In Page

### Page Description
Authentication page that allows users to either sign in to an existing account or create a new account. The sign-in and registration forms are inside the same HTML page and use JavaScript to switch between the two, which users navigate by using the Sign In and Sign Up buttons.

### Parameters Needed for the Page
**For sign in:**
- Username or email
- Password

**For sign up:**
- Username
- Email
- Password
- Confirm password

### Data Needed to Render the Page
- Validation messages
- Login error messages
- Registration error messages
- Existing usernames and emails checked when a user registers

### Link Destinations for the Page
- Dashboard after successful login
- Dashboard or confirmation state once a user registers
- Sign In view
- Sign Up view

### Tests for Verifying the Rendering of the Page
- Verify that validation messages match the input users entered.
- Verify that invalid login messages render when required fields are missing or incorrect.
- Verify that successful login sends the user to the dashboard.
- Verify that new user information is correctly added to the database.
- Verify that the Sign In and Sign Up views switch correctly.

### Mockup
<img width="1913" height="887" alt="41ef4ee5-f345-4c3f-b641-cc224d9ed6eb" src="https://github.com/user-attachments/assets/d211d0df-1c49-413a-bceb-69a6016a25b7" />
<img width="1914" height="877" alt="8ca6d3c9-387e-44e5-ad10-d043b051cd75" src="https://github.com/user-attachments/assets/81139e61-013b-47ef-865a-facd9f487244" />

---
# Page Title #2:
## Expenses Table Page

### Page Description
A table that has all the recorded expenses a user inputs. This table includes the expense amount, category, date of expense, and an optional description.

### Parameters Needed for the Page
- Logged-in user/session
- Optional category filter
- Optional date filter

### Data Needed to Render the Page
- `expense_id`
- Expense amount
- Expense category
- Expense date
- Expense description
- Logged-in user's `user_id`

### Link Destinations for the Page
- Dashboard
- Add Expense page
- Edit Expense action on page
- Delete Expense action on page
- User Information page

### Tests for Verifying the Rendering of the Page
- Verify that the expense table is displayed.
- Verify that expense amounts are rendered correctly.
- Verify that expense categories are rendered correctly.
- Verify that expense dates are rendered correctly.
- Verify that the total expense amount is rendered correctly.
- Verify that filtering options work correctly.
- Verify that descriptions are optional and render correctly.
- Verify that only the logged-in user's information is displayed.
- Verify that edited values are still saved after refreshing the page.
- Verify that deleting an expense removes it from the user's table.
- Verify that highlighting an expense for editing or deleting is rendered correctly.

### Mockup
+----------------------+-------------------------------------------------------------+
| Penny           | Expenses                                                  |
|                 |                                                           |
| [Dashboard]     | [Add]   Category: [Filter]   Date: [Filter]               |
| [Expenses]      | [Edit]                                                    |
| [Profile]       | +-------------------------------------------------------+ |
|                 | |Select | Date     | Description | Category      | Amount | 
|                 | +-------------------------------------------------------+ |
|                 | | [x]   |10/03/26 | Groceries   | Food           | $84.32 |        
|                 | | [x]   |10/05/26 | Gas         | Transportation | $42.10 |       
|                 | | [x]   |10/08/26 | Spotify     | Entertainment  | $11.99 |        
|                 | | [x]   |10/12/26 | Coffee      | Food           |  $6.25 |        
|                 | +-------------------------------------------------------+ |
|                 |                                                           |
|                 |                                   Total Expenses: $144.66 |
|                 |                                                           |
|                 |  [Plus button task bar option]                            |
|                 |                                                           |
| [Sign Out]      |                                   [Previous]  1  [Next]   |
+-----------------+-------------------------------------------------------------+

---
# Page Title #3:
## Dashboard Page
### Page Description
Includes reports of the user's recorded expenses. This might include graphs such as total spending per category, total expenses per month, and other graphs that the user might find useful.

### Parameters Needed for the Page
- Logged-in user/session
- Optional filters like date range and category
- Optional graph settings

### Data Needed to Render the Page
- Expense information from the database for the logged-in user
- Expense amounts
- Expense categories
- Expense dates

### Link Destinations for the Page
- Expenses Table page
- Add Expense page
- User Information page
- Sign Out

### Tests for Verifying the Rendering of the Page
- Verify that the dashboard loads correctly.
- Verify that the user can update graph parameters based on existing information.
- Verify that total expense amounts are displayed correctly.
- Verify that graph visualizations render correctly.
- Verify that only the logged-in user's information is displayed.
- Verify that removed data from the table is also removed from dashboard graphs.
- Verify that added or edited data is updated in the dashboard graphs.
- Verify that an empty message is displayed if no expense information exists.
- Verify that charts and summaries are rendered correctly.

### Mockup
+----------------------+----------------------------------------------------+
| Penny           | Dashboard                                               |
|                 |                                                         |
| [Dashboard]     | Category: [Filter]   Date: [Filter]                     |
| [Expenses]      |                                                         |
| [Profile]       | +-------------------+   +-------------------+           |
|                 | | Box 1             |   | Box 2             |           |
|                 | |                   |   |                   |           |
|                 | |    graph here     |   |    graph here     |           |
|                 | |                   |   |                   |           |
|                 | | Filter: []        |   | Filter: []        |           |
|                 | +-------------------+   +-------------------+           |
|                 |                                                         |
|                 | +-------------------+   +-------------------+           |
|                 | | Box 3             |   | Box 4             |           |
|                 | |                   |   |                   |           |
|                 | |    graph here     |   |    graph here     |           |
|                 | |                   |   |                   |           |
|                 | | Filter: []        |   | Filter: []        |           |
|                 | +-------------------+   +-------------------+           |
|                 |                                                         |
| [Sign Out]      |                                                         |
+-----------------+---------------------------------------------------------+

---
# Page Title #4:
## Add Expenses Page

### Page Description
A small pop-up form that allows the user to manually add a new expense or add a new category to track. The user can enter information about the expense or switch to the Add Category section to create a new category.

### Parameters Needed for the Page
- Expense amount
- Expense date
- Expense description
- Selected category
- New category name if the user creates one

### Data Needed to Render the Page
- Preexisting categories
- Manually added categories
- Validation messages
- Error messages if required fields are missing
- Logged-in user's `user_id`

### Link Destinations for the Page
- Expenses Table page
- Dashboard
- Add Category section
- Cancel/close action

### Tests for Verifying the Rendering of the Page
- Verify that the expense amount field is displayed.
- Verify that the expense date field is displayed.
- Verify that the description field is displayed.
- Verify that existing categories are displayed.
- Verify that manually added categories are displayed.
- Verify that the user can switch to the Add Category section.
- Verify that error messages appear when required fields are missing.
- Verify that invalid expense amounts show an error.
- Verify that a successfully added expense appears in the Expenses Table page.
- Verify that a new category appears as an option after it is added.

### Mockup
+----------------------+-------------------------------------------------------------+
| Penny                |        Add Expense         |        Add Category            |
|                      |  ---------------------------------------------------------  |                                                    
| [Dashboard]          |   Expense Name        [ New Expense____________________]    |
| [Expenses]           |   Description         [ ______________________________ ]    |
| [Profile]            |   Expense Amount      [ ______________________________ ]    |
|                      |   Expense Date        [ __ / __ / ____ ]                    |
|                      |   Category            [ Select Category ]                   |
|                      |                                                             |
|                      |                                                             |
|                      |   [ ] Add another                  [Cancel]   [Save]        |
|                      |                                                             |
|                      |                                                             |
| [Sign Out]           |                                                             |
+----------------------+-------------------------------------------------------------+

+----------------------+-------------------------------------------------------------+
| Penny                |        Add Expense         |        Add Category            |
|                      |  ---------------------------------------------------------  |                                                    
| [Dashboard]          |                                                             |
| [Expenses]           |   New Category            [ Manually input  ]               |
| [Profile]            |                                                             |
|                      |                                                             |
|                      |                                                             |
|                      |                                                             |
|                      |                                                             |
|                      |   [ ] Add another                  [Cancel]   [Save]        |
|                      |                                                             |
|                      |                                                             |
| [Sign Out]           |                                                             |
+----------------------+-------------------------------------------------------------+

---
# Page Title #5:
## User Information Page

### Page Description
Allows the user to view and update their account information.

### Parameters Needed for the Page
- Username
- Email
- Current password if needed
- New password if the user wants to change it
- Confirm new password

### Data Needed to Render the Page
- Logged-in user's current username
- Logged-in user's current email
- Validation messages
- Confirmation messages after information is updated

### Link Destinations for the Page
- Dashboard
- Expenses Table page
- Sign Out

### Tests for Verifying the Rendering of the Page
- Verify that the user's current username is displayed.
- Verify that the user's current email is displayed.
- Verify that editable account fields are shown.
- Verify that validation messages appear for invalid input.
- Verify that duplicate username or email errors display correctly.
- Verify that updated information is shown after saving.
- Verify that a confirmation message appears after the user's information is updated.

### Mockup
+----------------------+-------------------------------------------------------------+
| Penny           | Profile                                                   |
|                 |                                                           |
| [Dashboard]     | User Information                                          |
| [Expenses]      | Username:                                                 |
| [Profile]       | [_Username ________________]                              |
|                 |                                                           | 
|                 | Email:                                                    |
|                 | [Email Email_______________]                              |
|                 |                                                           |
|                 | Password
|                 | [Confirm Password _________]                              |
|                 | [Change Password]                                         |        
|                 | [Confirm Changed Password _]                              |     
|                 |                                                           |
|                 |                                                           |
|                 |                                                           |
|                 |                                                           |
| [Sign Out]      |                              [Cancel]    [Save Changes]   |
+-----------------+-----------------------------------------------------------+

