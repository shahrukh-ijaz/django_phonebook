from django.test import TestCase
from contacts.models import Contact, Number, Email, User


class ContactTestCase(TestCase):
    def setUp(self):
        Contact.objects.create(first_name="shahrukh", last_name="ijaz", note="mine")

    def test_contact_create(self):
        """contact could be created are correctly identified"""
        first_name = Contact.objects.get(first_name="shahrukh")
        self.assertEqual(first_name.test_contact_create(), 'The contact can be created!')
