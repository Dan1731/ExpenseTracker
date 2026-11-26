#Author: Layce Smith
#Purpose: Test the profile functionality of the Penny application.
#Usage: Run this test file to ensure that the profile route correctly displays the profile page and handles session management.


import unittest
from app import create_app
from init_extension import db

class TestProfile(unittest.TestCase):
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

    def test_profile_page_accessible(self):
        # Simulate a user login by setting a session variable.
        with self.client.session_transaction() as sess:
            sess["username"] = "testuser"

        # Access the profile page.
        response = self.client.get("/profile")

        # Check that the response is successful (status code 200).
        self.assertEqual(response.status_code, 200)

    def test_profile_page_redirects_when_not_logged_in(self):
        # Access the profile page without logging in.
        response = self.client.get("/profile", follow_redirects=True)

        # Check that the response redirects to the login page (status code 200 after redirect).
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Login", response.data)  # Assuming the login page contains the word "Login"

    def test_profile_page_content(self):
        # Simulate a user login by setting a session variable.
        with self.client.session_transaction() as sess:
            sess["username"] = "
