from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from expenses.models import Expense
from django.contrib.auth.models import User
import re


def validate_custom_password(password):
    """
    Custom password validation:
    - Must contain at least one special character.
    """
    errors = []

    if not re.search(r"\W", password):
        errors.append("Password must contain at least one special character.")

    return errors


def validate_username(username):
    """
    Custom username validation:
    - Must contain at least 4 alphanumeric characters.
    """
    errors = []

    if not re.search(r"[a-zA-Z0-9]{4,}", username):
        errors.append("Your username must contain at least 4 alphanumeric characters.")

    return errors


def signup_view(request):
    template = "signup.html"

    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        username = request.POST.get("username", "")
        password = request.POST.get("password1", "")
        error_labels = set()

        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            error_labels.add("A user with that username already exists.")
        else:
            # Validate username
            username_errors = validate_username(username)
            error_labels.update(username_errors)

            # Validate password only if username is valid
            if not username_errors:
                password_errors = validate_custom_password(password)
                error_labels.update(password_errors)

        # If form is valid and no additional errors, proceed
        if form.is_valid() and not error_labels:
            user = form.save()
            login(request, user)
            return redirect("expenses:home")

        # Add Django form validation errors
        for errors in form.errors.values():
            error_labels.update(errors)

        request.session["errors"] = list(error_labels)  # Store errors in session
        return redirect("accounts:signup")  # Redirect to clear the form on reload

    # Clear errors after first reload
    errors = request.session.pop("errors", [])

    context = {"form": UserCreationForm(), "errors": errors}
    return render(request, template, context)


def logout_view(request):
    # Delete testuser data to start from scratch when testing.
    Expense.objects.deleteTestuserExpenses(request)
    Expense.objects.deleteTestuserBudget(request)

    logout(request)
    return redirect("expenses:home")
