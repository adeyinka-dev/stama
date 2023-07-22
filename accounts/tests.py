from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class ManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create(
            username="testuser",
            email="testuser@example.com",
            password="testpass1234",
            dob="2007-07-07",
            matric_num="12345678",
            faculty="CAD",
            department="Medicine",
            phone_number="12345678910",
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertEqual(user.dob, "2007-07-07")
        self.assertEqual(user.matric_num, "12345678")
        self.assertEqual(user.faculty, "CAD")
        self.assertEqual(user.department, "Medicine")
        self.assertEqual(user.phone_number, "12345678910")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="testsuperuser",
            email="testsuperuser@example.com",
            password="testpass1234",
        )

        self.assertEqual(admin_user.username, "testsuperuser")
        self.assertEqual(admin_user.email, "testsuperuser@example.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignUpPageTests(TestCase):
    def test_signup_url_location_is_correct(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
