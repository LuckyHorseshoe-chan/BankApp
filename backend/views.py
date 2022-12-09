from django.shortcuts import render
from .models import User, Currency, Country, Bank, Check, Operation, Active

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_users = User.objects.all().count()
    num_checks = Check.objects.all().count()

    # Available users
    num_unblocked_users = User.objects.filter(blocked__exact=False).count()

    context = {
        'num_users': num_users,
        'num_checks': num_checks,
        'num_unblocked_users': num_unblocked_users,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
