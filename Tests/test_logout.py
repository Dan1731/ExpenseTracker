#Author: Layce Smith
#Purpose: Test the logout functionality of the Penny application.
#Usage: Run this test file to ensure that the logout route correctly clears the session and redirects to the login page.

###run with: python -m unittest Tests/test_logout.py

import unittest
from app import create_app
from init_extension import db

class TestLogout(unittest.TestCase):
    def setUp(self):
        self.app = create_app({
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"  # Test in-memory database using SQLite
        })

        self.context = self.app.app_context()
        self.context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.context.pop()

    def test_logout_clears_session(self):
        # Simulate a user login by setting a session variable.
        with self.client.session_transaction() as sess:
            sess["username"] = "testuser"

        # Ensure the session variable is set before logout.
        with self.client.session_transaction() as sess:
            self.assertIn("username", sess)

        # Perform the logout action.
        response = self.client.get("/logout", follow_redirects=True)

        # Check that the session variable is cleared after logout.
        with self.client.session_transaction() as sess:
            self.assertNotIn("username", sess)

        # Check that the response redirects to the login page.
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Login", response.data)  # Assuming the login page contains the word "Login" 




