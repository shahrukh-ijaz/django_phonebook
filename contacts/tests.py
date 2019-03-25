from django.test import TestCase

from contacts.forms import AddContactForm
from contacts.models import Contact, Number, Email, User


class ContactTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='sharukh999', password='shahrukh31')
        Contact.objects.create(first_name='shahrukh', last_name='ijaz', note='mine', dob='2019-03-14', user_id=user)

    def test_to_delete_contact(self):
        users = Contact.objects.filter(user_id=2).count()
        if users > 0:
            self.assertFalse(users, 'The contact have contacts able to delete!')
        else:
            self.assertFalse(users, 'The contact have contacts not able to delete!')

    def test_invalid_form(self):
        user = User.objects.create(username='sharukh', password='shahrukh31')
        w = Contact.objects.create(first_name='shahrukh', last_name='ijaz', note='mine', dob='2019-03-14', user_id=user)
        form = AddContactForm()
        self.assertFalse(form.is_valid())


class EmailTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='sharrukh9990', password='shahrukh31')
        contact = Contact.objects.create(first_name='shahrukh', last_name='ijaz', note='mine', dob='2019-03-14', user_id=user)

    def test_successEmail(self):
        user = User.objects.create(username='sharuukh9990', password='shahrukh31')
        contact = Contact.objects.create(first_name='shahrukh', last_name='ijaz', note='mine', dob='2019-03-14', user_id=user)
        email = Email.objects.create(email='shahrukh.ijaz@arbisoft.com', contact_id=contact)
        self.assertEqual('Email Created!', 'Email Created!')


class NumberTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='sharukhu9990', password='shahrukh31')
        contact = Contact.objects.create(first_name='shahrukh', last_name='ijaz', note='mine', dob='2019-03-14', user_id=user)

    def test_successNumber(self):

        user = User.objects.create(username='sharukhuu9990', password='shahrukh31')
        contact = Contact.objects.create(first_name='shahrukh', last_name='ijaz', note='mine', dob='2019-03-14',
                                         user_id=user)
        email = Number.objects.create(number='03209503962', contact_id=contact)
        self.assertEqual('Number Created!', 'Number Created!')
