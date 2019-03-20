from django.test import TestCase

from contacts.forms import AddContactForm
from contacts.models import Contact, Number, Email, User
from django.contrib.auth.models import User


class ContactTestCase(TestCase):

    def setUp(self):
        user = User(username='sharukh', password='shahrukh31')
        user.save()
        Contact.objects.create(first_name="shahrukh", last_name="ijaz", note="mine",  dob='2019-03-14', user_id=user)

    def able_to_delete_contact(self):
        users = Contact.objects.filter(user_id=2).count()
        if users > 0:
            self.assertFalse(users, 'The contact have contacts able to delete!')
        else:
            self.assertFalse(users, 'The contact have contacts not able to delete!')

    def test_invalid_form(self):
        user = User(username='sharukh9990', password='shahrukh31')
        user.save()
        w = Contact.objects.create(first_name="shahrukh", last_name="ijaz", note="mine", dob='2019-03-14', user_id=user)
        form = AddContactForm()
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
