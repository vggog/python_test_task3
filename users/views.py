from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .forms import UserRegistrationForm


def register(request: HttpRequest) -> HttpResponse:
    """Views for registration"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(
                request,
                'register_done.html',
                {'new_user': new_user},
            )

    else:
        user_form = UserRegistrationForm()

    return render(
        request,
        'register.html',
        {'user_form': user_form},
    )
