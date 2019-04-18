from django.test import TestCase
from contacts.forms import AddContactForm
from contacts.models import Contact, Number, Email, User


class ContactTestCase(TestCase):

    def test_to_delete_contact(self):
        users = Contact.objects.filter(user_id=2).count()
        if users > 0:
            self.assertFalse(users, 'The contact have contacts able to delete!')
        else:
            self.assertFalse(users, 'The contact have contacts not able to delete!')

    def test_valid_form(self):
        form = AddContactForm(data={'user_email': "user@mp.com", 'password': "user", 'first_name': "shahrukh",
                                    'last_name': "ijaz", 'contact_number': '03209503962', 'note': 'mine',
                                    'dob': '2019-03-14'})
        self.assertTrue(form.is_valid())

    def test_invalid_password(self):
        form = AddContactForm(data={'email': "user@mp.com", 'password': "", 'first_name': "shahrukh",
                                    'last_name': "ijaz", 'contact_number': '03209503962', 'note': 'mine',
                                    'dob': '2019-03-14'})
        self.assertFalse(form.is_valid())

    def test_invalid_email(self):
        form = AddContactForm(data={'email': "", 'password': "user", 'first_name': "shahrukh",
                                    'last_name': "ijaz", 'contact_number': '03209503962', 'note': 'mine',
                                    'dob': '2019-03-14'})
        self.assertFalse(form.is_valid())

    def test_invalid_dob(self):
        form = AddContactForm(data={'email': "user@mp.com", 'password': "123", 'first_name': "shahrukh",
                                    'last_name': "ijaz", 'contact_number': '03209503962', 'note': 'mine',
                                    'dob': ''})
        self.assertFalse(form.is_valid())

    def test_invalid_contact_number(self):
        form = AddContactForm(data={'email': "user@mp.com", 'password': "user", 'first_name': "shahrukh",
                                    'last_name': "ijaz", 'contact_number': '', 'note': 'mine',
                                    'dob': '2019-03-14'})
        self.assertFalse(form.is_valid())

    def test_invalid_note(self):
        form = AddContactForm(data={'email': "user@mp.com", 'password': "user", 'first_name': "shahrukh",
                                    'last_name': "ijaz", 'contact_number': '03209503962', 'note': '',
                                    'dob': '2019-03-14'})
        self.assertFalse(form.is_valid())


class EmailTestCase(TestCase):

    def test_success_email(self):
        user = User.objects.create(username='sharuukh9990', password='shahrukh31')
        contact = Contact.objects.create(first_name='shahrukh', last_name='ijaz', note='mine', dob='2019-03-14', user_id=user)
        Email.objects.create(email='shahrukh.ijaz@arbisoft.com', contact_id=contact)
        self.assertEqual('Email Created!', 'Email Created!')


class NumberTestCase(TestCase):

    def test_success_number(self):

        user = User.objects.create(username='sharukhuu9990', password='shahrukh31')
        contact = Contact.objects.create(first_name='shahrukh', last_name='ijaz', note='mine', dob='2019-03-14',
                                         user_id=user)
        Number.objects.create(number='03209503962', contact_id=contact)
        self.assertEqual('Number Created!', 'Number Created!')

