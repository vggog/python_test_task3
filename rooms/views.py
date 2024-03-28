from django.http import HttpResponse
from django.shortcuts import render

from .service import Service


def all_rooms(request) -> HttpResponse:
    service = Service()

    context = {
        'rooms': service.get_all_rooms(),
    }

    return render(
        request,
        'rooms.html',
        context
    )
