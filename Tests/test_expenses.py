import unittest
from datetime import date
from decimal import Decimal

from app import create_app
from init_extension import db
from models import ExpenseTrans

class TestExpenses(unittest.TestCase):
    ### Runs before every test.
    def setUp(self):
        self.app = create_app({
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:" # Test in-memory database using SQLite
        })

        ### Creates a test client that mocks a HTTP request.
        self.context = self.app.app_context()
        self.context.push()
        self.client = self.app.test_client()

        ### Mock expense data:
        self.expenses = [
            {
                "date": date(2026, 11, 5),
                "expense": "Coffee",
                "category": "Food", ### Placeholder until confirmed categories are set.
                "amount": Decimal("8.50")
            },

            {
                "date": date(2026, 11, 7),
                "expense": "Gas",
                "category": "Transport",
                "amount": Decimal("25.00")
            },

            {
                "date": date(2026, 11, 8),
                "expense": "Groceries",
                "category": "Food",
                "amount": Decimal("125.60")
            },

            {
                "date": date(2026, 11, 9),
                "expense": "Internet",
                "category": "Utilities",
                "amount": Decimal("70.51")
            },

            {
                "date": date(2026, 11, 11),
                "expense": "Lunch",
                "category": "Food",
                "amount": Decimal("15.00")
            },

            {
                "date": date(2026, 11, 4),
                "expense": "Car Repair",
                "category": "Transport",
                "amount": Decimal("200.00")
            },

            {
                "date": date(2026, 10, 30),
                "expense": "Rent",
                "category": "Housing",
                "amount": Decimal("2500.00")
            }
        ]

    ### Runs after every test.
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.context.pop()


    ### Expense Calculation Tests ###
    # To Do whenever Miles completes button logic.
    #
    # def test_calculation_returnsTotalExpenses(self):
        # response = self.client.get("/expenses")
        # self.assertEqual(response.status_code, 200)
        # self.assertIn(b"$2,944.61", response.data)

    # def test_overview_returnsLargestExpense
        # response = self.client.get("/expenses")
    
        # self.assertEqual(response.status_code, 200)
        # Verify that summary-largest displays $2,500.00.

    # Should we do overall total transactions or within range?
    # def test_overview_returnsTotalTransactions
        # response = self.client.get("/expenses")
        # self.assertEqual(response.status_code, 200)
        # Verify that i count = total transactions

    ### DATE FILTER TESTS ###
    # Verify that only expenses from November 5-11 are included.
    # Five expenses should be included. Two should be excluded.
    # Expected total: $244.61
    # def test_lastSevenDays_returnsCorrectTotal(self):
        # response = self.client.get("/expenses", query_string={
            # "start_date": "2026-11-05",
            # "end_date": "2026-11-11"
        # })

        # self.assertEqual(response.status_code, 200)
        # self.assertIn(b"$244.61", response.data)
        # self.assertNotIn(b"Car Repair", response.data)
        # self.assertNotIn(b"Rent", response.data)

    # Verify start and end dates return correct expenses.
    # November 7-9 should include Gas, Groceries, and Internet.
    # Expected total: $221.11
    # def test_dateRange_returnsThreeExpenses(self):
        # response = self.client.get("/expenses", query_string={
            # "start_date": "2026-11-07",
            # "end_date": "2026-11-09"
        # })
    
        # self.assertEqual(response.status_code, 200)
        # self.assertIn(b"Gas", response.data)
        # self.assertIn(b"Groceries", response.data)
        # self.assertIn(b"Internet", response.data)
        # self.assertNotIn(b"Coffee", response.data)
        # self.assertNotIn(b"Rent", response.data)

    ### CATEGORY FILTER TESTS ###
    # Enable when category filtering is implemented.
    # Verify that selecting Food only returns Food expenses.
    # Expected expenses: Coffee, Groceries, Lunch.
    # Expected count: 3
    # Expected total: $149.10
    # def test_categoryFilter_returnsThreeExpenses(self):
        # response = self.client.get("/expenses", query_string={
            # "category": "Food"
        # })

        # self.assertEqual(response.status_code, 200)
        # self.assertIn(b"Coffee", response.data)
        # self.assertIn(b"Groceries", response.data)
        # self.assertIn(b"Lunch", response.data)
        # self.assertNotIn(b"Gas", response.data)
        # self.assertNotIn(b"Rent", response.data)

    ### ACTIONS TESTS ###
    # def test_deleteExpense_returnsTotalExistingExpenses(self):

    # def test_editExpense_returnsTotalExistingExpenses(self):
        # Verify a duplicate isn't made
        # Verify total expense amount gets updated
    
    # def test_createExpense_returnsTotalExistingExpenses(self):
        # Verify total expenses = i + 1
        # Verify transactions = i + 1
        # Verify largest expense gets updated

if __name__ == "__main__":
    unittest.main()