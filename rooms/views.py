from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .service import Service
from .forms import FilterAndSortForm


def all_rooms(request: HttpRequest) -> HttpResponse:
    service = Service()

    rooms = service.get_all_rooms()
    if request.method == 'POST':
        form = FilterAndSortForm(request.POST)
        if form.is_valid():
            rooms = service.get_rooms_with_sorting_and_filtering(form)
    else:
        form = FilterAndSortForm()

    context = {
        'rooms': rooms,
        'form': form,
    }

    return render(
        request,
        'rooms.html',
        context
    )


def get_room(request: HttpRequest, room_id: int) -> HttpResponse:
    """Вьюха для получения информации о комнате"""
    service = Service()
    room = service.get_room(room_id)
    if room is None:
        return HttpResponse('Room doesn\'t found')

    context = {
        'room': room,
        'unbooked_dates': service.get_unbooked_days(room_id)
    }

    return render(
        request,
        'room.html',
        context
    )
