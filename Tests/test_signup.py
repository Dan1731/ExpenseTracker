import unittest

from app import create_app
from email_validator import validate_email
from init_extension import db
from models import User
from unittest.mock import patch
from werkzeug.security import generate_password_hash, check_password_hash

class TestSignup(unittest.TestCase):
    def setUp(self):
        self.app = create_app({
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
        })

        self.context = self.app.app_context()
        self.context.push()

        self.client = self.app.test_client()
        self.email_patch = patch(
            "login_route.validate_email",
            side_effect=self.validate_test_email
        )
        self.email_patch.start()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.email_patch.stop()
        self.context.pop()

    def validate_test_email(self, email, **kwargs):
        return validate_email(email, check_deliverability=False)

    ### MISSING TESTS ###
    def test_missingFirstName_returnsErrorMessage(self):
        response = self.client.post("/signup", data={
            "first_name": "",
            "last_name": "Smith",
            "username": "johnsmith",
            "email": "test@example.com",
            "password": "Password123",
            "confirm_password": "Password123"
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Please enter your first name.", response.data)

    def test_missingLastName_returnsErrorMessage(self):
        response = self.client.post("/signup", data={
                    "first_name": "John",
                    "last_name": "",
                    "username": "johnsmith",
                    "email": "test@example.com",
                    "password": "Password123",
                    "confirm_password": "Password123"
                })
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Please enter your last name.", response.data)

    def test_missingUserName_returnsErrorMessage(self):
        response = self.client.post("/signup", data={
                    "first_name": "John",
                    "last_name": "Smith",
                    "username": "",
                    "email": "test@example.com",
                    "password": "Password123",
                    "confirm_password": "Password123"
                })
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Please enter a unique username.", response.data)

    def test_missingEmail_returnsErrorMessage(self):
        response = self.client.post("/signup", data={
                    "first_name": "John",
                    "last_name": "Smith",
                    "username": "johnsmith",
                    "email": "",
                    "password": "Password123",
                    "confirm_password": "Password123"
                })
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Please enter a valid email.", response.data)

    def test_missingPassword_returnsErrorMessage(self):
        response = self.client.post("/signup", data={
                    "first_name": "John",
                    "last_name": "Smith",
                    "username": "johnsmith",
                    "email": "test@example.com",
                    "password": "",
                    "confirm_password": "Password123"
                })
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Password must be 8 to 20 characters long", response.data)

    def test_missingConfirmPassword_returnsErrorMessage(self):
        response = self.client.post("/signup", data={
                    "first_name": "John",
                    "last_name": "Smith",
                    "username": "johnsmith",
                    "email": "test@example.com",
                    "password": "Password123",
                    "confirm_password": ""
                })
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Please confirm your password.", response.data)

    ### USERNAME VALIDATION TESTS ###
    def test_usernameTooShort_returnsErrorMessage(self):
        response = self.client.post("/signup", data={
                    "first_name": "John",
                    "last_name": "Smith",
                    "username": "joh",
                    "email": "test@example.com",
                    "password": "Password123",
                    "confirm_password": ""
                })
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Username must be between 4 and 15 characters.", response.data)

    def test_usernameTooLong_returnsErrorMessage(self):
        response = self.client.post("/signup", data={
                    "first_name": "John",
                    "last_name": "Smith",
                    "username": "somanytestssolittletime",
                    "email": "test@example.com",
                    "password": "Password123",
                    "confirm_password": ""
                })
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Username must be between 4 and 15 characters.", response.data)

    def test_usernameFormatting_normalizesUsername(self):
        response = self.client.post("/signup", data={
                    "first_name": "John",
                    "last_name": "Smith",
                    "username": "how dare you!",
                    "email": "test@example.com",
                    "password": "Password123",
                    "confirm_password": "Password123"
                })
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Username cannot contain special characters or spacing.", response.data)

    ### EMAIL VALIDATION TESTS ###
    def test_invalidEmail_returnsErrorMessage(self):
        response = self.client.post("/signup", data={
            "first_name": "John",
            "last_name": "Smith",
            "username": "johnsmith",
            "email": "notanemail",
            "password": "Password123",
            "confirm_password": "Password123"
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Please enter a valid email address.", response.data)

    ### PASSWORD VALIDATION TESTS ###

    def test_passwordTooShort_returnsErrorMessage(self):
        response = self.client.post("/signup", data={
            "first_name": "John",
            "last_name": "Smith",
            "username": "johnsmith",
            "email": "test@example.com",
            "password": "Pass1",
            "confirm_password": "Pass1"
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Password must be 8 to 20 characters long.", response.data)

    def test_passwordTooLong_returnsErrorMessage(self):
        response = self.client.post("/signup", data={
            "first_name": "John",
            "last_name": "Smith",
            "username": "johnsmith",
            "email": "test@example.com",
            "password": "Password123456789012345",
            "confirm_password": "Password123456789012345"
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Password must be 8 to 20 characters long.", response.data)

    def test_passwordMissingUppercase_returnsErrorMessage(self):
        response = self.client.post("/signup", data={
            "first_name": "John",
            "last_name": "Smith",
            "username": "johnsmith",
            "email": "test@example.com",
            "password": "password123",
            "confirm_password": "password123"
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Password must have an uppercase letter.", response.data)

    def test_passwordMissingLowercase_returnsErrorMessage(self):
        response = self.client.post("/signup", data={
            "first_name": "John",
            "last_name": "Smith",
            "username": "johnsmith",
            "email": "test@example.com",
            "password": "PASSWORD123",
            "confirm_password": "PASSWORD123"
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Password must have a lowercase letter.", response.data)

    def test_passwordMissingNumber_returnsErrorMessage(self):
        response = self.client.post("/signup", data={
            "first_name": "John",
            "last_name": "Smith",
            "username": "johnsmith",
            "email": "test@example.com",
            "password": "PasswordABC",
            "confirm_password": "PasswordABC"
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Password must contain a number.", response.data)

    def test_passwordMismatch_returnsErrorMessage(self):
        response = self.client.post("/signup", data={
            "first_name": "John",
            "last_name": "Smith",
            "username": "johnsmith",
            "email": "test@example.com",
            "password": "Password123",
            "confirm_password": "Different123"
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Passwords do not match.", response.data)

    ### Existing User Tests ###
    def test_existingUsername_returnsErrorMessage(self):
        with self.app.app_context():
            existing_user = User(
                first_name="Jane",
                last_name="Doe",
                username="newuser",
                email="existing@example.com",
                password_hash=generate_password_hash("Password123")
            )

            db.session.add(existing_user)
            db.session.commit()

        response = self.client.post("/signup", data={
            "first_name": "John",
            "last_name": "Smith",
            "username": "NewUser",
            "email": "test@example.com",
            "password": "Password123",
            "confirm_password": "Password123"
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Username is already taken.", response.data)

    def test_existingEmail_returnsErrorMessage(self):
        with self.app.app_context():
            existing_user = User(
                first_name="Jane",
                last_name="Doe",
                username="janedoe",
                email="test@example.com",
                password_hash=generate_password_hash("Password123")
            )

            db.session.add(existing_user)
            db.session.commit()

        response = self.client.post("/signup", data={
            "first_name": "John",
            "last_name": "Smith",
            "username": "johnsmith",
            "email": "test@example.com",
            "password": "Password123",
            "confirm_password": "Password123"
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Seems like you already have an account!",
            response.data
        )

    ### SUCCESSFUL REGISTRATION TESTS ###

    def test_validSignup_createsUser(self):
        response = self.client.post("/signup", data={
            "first_name": "John",
            "last_name": "Smith",
            "username": "johnsmith",
            "email": "test@example.com",
            "password": "Password123",
            "confirm_password": "Password123"
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Account created successfully!", response.data)

        with self.app.app_context():
            user = db.session.execute(
                db.select(User).filter_by(username="johnsmith")
            ).scalar_one_or_none()

            self.assertIsNotNone(user)
            self.assertEqual(user.first_name, "John")
            self.assertEqual(user.last_name, "Smith")
            self.assertEqual(user.email, "test@example.com")

    def test_validSignup_hashesPassword(self):
        response = self.client.post("/signup", data={
            "first_name": "John",
            "last_name": "Smith",
            "username": "johnsmith",
            "email": "test@example.com",
            "password": "Password123",
            "confirm_password": "Password123"
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Account created successfully!", response.data)

        with self.app.app_context():
            user = db.session.execute(
                db.select(User).filter_by(username="johnsmith")
            ).scalar_one_or_none()

            self.assertIsNotNone(user)
            self.assertNotEqual(user.password_hash, "Password123")
            self.assertTrue(
                check_password_hash(user.password_hash, "Password123")
            )

    ### ROUTING TESTS ###

    def test_signupGET_displaysRegistrationPage(self):
        response = self.client.get("/signup")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<form", response.data)

if __name__ == "__main__":
    unittest.main()
