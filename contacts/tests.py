from django.test import TestCase
from contacts.models import Contact, Number, Email, User


class ContactTestCase(TestCase):
    def setUp(self):
        Contact.objects.create(first_name="shahrukh", last_name="ijaz", note="mine")

    def test_contact_create(self):
        contact = Contact.objects.get(first_name="shahrukh")
        self.assertEqual(contact.test_contact_create(), 'The contact can be created!')

    def able_to_delete_contact(self):
        users = Contact.objects.filter(user_id=2).count()
        if users > 0:
            self.assertEqual(users, 'The contact have contacts able to delete!')
        else:
            self.assertFalse(users, 'The contact have contacts not able to delete!')

    def test_invalid_form(self):
        w = Contact.objects.create(first_name="shahrukh", last_name="ijaz", note="mine")
        data = {'first_name': w.first_name, 'last_name': w.last_name, 'note': w.note, }
        form = Contact(data=data)
        self.assertFalse(form.is_valid())


class EmailTestCase(TestCase):
    def setUp(self):
        Email.objects.create(Email='shahrukh.ijaz@arbisoft.com', contact_id=1)

    def ErrorEmail(self):
        email = Email.objects.get(Email="shahrukh.ijaz@arbisoft.com")
        self.assertFalse(email, 'The email not belong to any Contact')

    def SuccessEmail(self):
        email = Email.objects.create(Email='shahrukh.ijaz@arbisoft.com', contact_id=1)
        self.assertEqual(email, 'Email Created!')


class NumberTestCase(TestCase):
    def setUp(self):
        Number.objects.create(Number='03209503962', contact_id=1)

    def ErrorNumber(self):
        number = Number.objects.get(Number='03209503962')
        self.assertFalse(number, 'The Number not belong to any Contact')

    def SuccessNumber(self):
        number = Number.objects.create(Number='03209503962', contact_id=1)
        self.assertEqual(number, 'Number Created!')
