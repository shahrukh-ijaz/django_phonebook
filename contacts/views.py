from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseRedirect

from contacts.forms import AddContactForm, SignUpForm
from contacts.models import Contact, Email, Number
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required



@login_required
@require_http_methods(["POST", "GET"])
def add_contact(request):
    if request.method == "GET":
        form = AddContactForm()
        return render(request, 'contacts/add_contact.html', {'form': form})
    else:
        form = AddContactForm(request.POST)
        if not form.is_valid():
            return render_to_response('contacts/add_contact.html', {'form': form})

        email = form.cleaned_data.get('user_email')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        note = form.cleaned_data.get('note')
        contact_number = form.cleaned_data.get('contact_number')
        dob = form.cleaned_data.get('dob')

        errors = list()

        if len(first_name) < 4:
            errors.append("Firstname is too short")

        if len(last_name) < 4:
            errors.append("Lastname is too short")

        if len(note) < 4:
            errors.append("note is too short")

        if len(contact_number) < 11:
            errors.append("contact_number is too short")

        if len(errors) > 0:
            return render(request, 'contacts/add_contact.html', {'form': form, 'errors': errors})

        user_id = request.user.id
        user = User.objects.get(id=user_id)
        contact = Contact(first_name=first_name, last_name=last_name, dob=dob, note=note, user_id=user)
        contact.save()

        email = Email(email=email, contact_id=contact)
        email.save()

        number = Number(number=contact_number, contact_id=contact)
        number.save()

        return HttpResponseRedirect('/user_index/')


@require_http_methods(["GET"])
@login_required
def edit(request, id):
    contact = Contact.objects.get(id=id)
    if contact is not None:
        return render(request, 'contacts/edit_contact.html', {'contact': contact, 'contact_id': id})


@require_http_methods(["GET"])
@login_required
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
    user_str = str(request.user)
    if request.user is not None:
        return HttpResponseRedirect('/user_index/')
    else:
        return HttpResponse('%s is not logged in' % user_str)


@login_required
def user_index(request):
    contact = Contact.objects.filter(user_id=request.user.id)
    return render(request, 'contacts/user_index.html', {'contacts': contact})


@login_required
@require_http_methods(["GET", "POST"])
def add_email(request, id=None):
    if request.method == "GET":
        return render(request, 'contacts/add_email.html', {'contact_id': id})
    else:
        email = request.POST.get('email')
        id = request.POST.get('contact_id')

        contact = Contact.objects.get(id=id)
        new_email = Email(email=email, contact_id=contact)
        new_email.save()
        return HttpResponseRedirect('/user_index/')

@login_required
@require_http_methods(["GET", "POST"])
def add_number(request, id=None):
    if request.method == "GET":
            return render(request, 'contacts/add_number.html', {'contact_id': id})
    else:
        number = request.POST.get('number')
        id = request.POST.get('contact_id')
        contact = Contact.objects.get(id=id)
        new_number = Number(number=number, contact_id=contact)
        new_number.save()
        return HttpResponseRedirect('/user_index/')


def display_contact(request, id=None):
    contact = Contact.objects.get(id=id)
    emails = Email.objects.filter(contact_id=contact)
    numbers = Number.objects.filter(contact_id=contact)
    return render(request, 'contacts/view_contact.html', {'contact': contact, 'emails': emails, 'numbers': numbers})


@login_required
@require_http_methods(["POST"])
def update_contact(request):
    id = request.POST.get('contact_id')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    note = request.POST.get('note')
    dob = request.POST.get('dob')

    contact = Contact.objects.get(id=id)
    if contact is not None:
        contact.first_name = first_name
        contact.last_name = last_name
        contact.dob = dob
        contact.note = note
        contact.save()
        return HttpResponseRedirect('/user_index/')


@login_required
def number_delete(request, id, contact_id):
    number = Number.objects.get(id=id)
    if number is not None:
        number.delete()
    return HttpResponseRedirect('/display_contact/'+contact_id)


@login_required
def email_delete(request, id, contact_id):
    email = Email.objects.get(id=id)
    if email is not None:
        email.delete()
    return HttpResponseRedirect('/display_contact/' + contact_id)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/user_index/')
    else:
        form = SignUpForm()
    return render(request, 'contacts/signup.html', {'form': form})
