from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseRedirect
from contacts.models import Contact, Email, Number
from django.contrib.auth.models import User


def index(request):
    return render(request, 'contacts/index.html')


def insert(request):
    return render(request, 'contacts/test.html')


def add_contact(request):
    if request.method == "POST":
        email = request.POST['user_email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        note = request.POST['note']
        contact_number = request.POST['contact_number']
        dob = request.POST['dob']

        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)

        contact = Contact(first_name=first_name, last_name=last_name, dob=dob, note=note, user_id=user)
        contact.save()

        email = Email(email=email, contact_id=contact)
        email.save()

        number = Number(number=contact_number, contact_id=contact)
        number.save()

        return HttpResponseRedirect('/user_index/', {'message': 'Deleted Successfully!!'})
    else:
        return HttpResponse("You're looking at GET")


def login(request):
    return render(request, 'contacts/login.html')


def logout(request):

    del request.session['username']
    del request.session['user_id']
    return HttpResponseRedirect('/')


def edit(request, id):
    contact = Contact.objects.get(id=id)
    if contact is not None:
        return render(request, 'contacts/edit_contact.html', {'contact': contact, 'contact_id': id})


def delete(request, id):
    contact = Contact.objects.get(id=id)
    if contact is not None:
        emails = Email.objects.filter(contact_id=id)
        numbers = Number.objects.filter(contact_id=id)
        if emails is not None and numbers is not None:
            emails.delete()
            numbers.delete()
            contact.delete()
            return HttpResponseRedirect('/user_index/')
    return HttpResponse("Not delete id issue while try delete")


def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.get(username=username, password=password)
    request.session['username'] = username
    request.session['user_id'] = user.id
    if user is not None:
        contact = Contact.objects.filter(user_id=user.id)
        return HttpResponseRedirect('/user_index/')
    else:
        return HttpResponseNotFound('<h1>not correct username/password</h1>')


def user_index(request):
    user_id = request.session['user_id']
    if user_id is not None:
        contact = Contact.objects.filter(user_id=user_id)
        return render(request, 'contacts/user_index.html', {'contacts': contact})


def add_email(request, id=None):
    if request.method == "GET":
        return render(request, 'contacts/add_email.html', {'contact_id': id})
    else:
        email = request.POST['email']
        id = request.POST['contact_id']

        contact = Contact.objects.get(id=id)
        new_email = Email(email=email, contact_id=contact)
        new_email.save()
        return HttpResponseRedirect('/user_index/')


def add_number(request, id=None):
    if request.method == "GET":
        return render(request, 'contacts/add_number.html', {'contact_id': id})
    else:
        number = request.POST['number']
        id = request.POST['contact_id']
        contact = Contact.objects.get(id=id)
        new_number = Number(number=number, contact_id=contact)
        new_number.save()
        return HttpResponseRedirect('/user_index/')


def view(request, id=None):
    contact = Contact.objects.get(id=id)
    emails = Email.objects.filter(contact_id=contact)
    numbers = Number.objects.filter(contact_id=contact)
    return render(request, 'contacts/view.html', {'contact': contact, 'emails': emails, 'numbers': numbers})


def update_contact(request):
    id = request.POST['contact_id']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    note = request.POST['note']
    dob = request.POST['dob']

    contact = Contact.objects.get(id=id)
    if contact is not None:
        contact.first_name = first_name
        contact.last_name = last_name
        contact.dob = dob
        contact.note = note
        contact.save()
        return HttpResponseRedirect('/user_index/')


def number_delete(request, id, contact_id):
    number = Number.objects.get(id=id)
    if number is not None:
        number.delete()
    return HttpResponseRedirect('/view/'+contact_id)


def number_edit(request, id, contact_id):
    number = Number.objects.get(id=id)
    return render('')
    return HttpResponseRedirect('/index/')


def email_delete(request, id, contact_id):
    email = Email.objects.get(id=id)
    if email is not None:
        email.delete()
    return HttpResponseRedirect('/view/' + contact_id)


def email_edit(request, id, contact_id):
    email = Email.objects.get(id=id)
    return render("contacts/email_edit.html", {'email': email, 'contact_id': contact_id})
