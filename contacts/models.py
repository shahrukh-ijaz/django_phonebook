from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    first_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=30, default="")
    note = models.TextField(max_length=300, default="")
    dob = models.DateField()

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Email(models.Model):
    email = models.EmailField(default='example@example.com')
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.email


class Number(models.Model):
    number = models.CharField(max_length=15, default='SOME STRING2' )
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE)

