from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.contrib.auth import get_user
from django.contrib.auth.models import AnonymousUser

from .service import Service
from .forms import FilterAndSortForm, BookingRecordForm


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
    form = BookingRecordForm()
    info = ''

    if room is None:
        return HttpResponse('Room doesn\'t found')

    if request.method == 'POST':
        form = BookingRecordForm(request.POST)
        user = get_user(request)
        if user is AnonymousUser:
            info = 'Создать бронь может только авторизированный пользователь.'

        elif form.is_valid():
            info = service.book_date(
                date_from=form.cleaned_data['data_from'],
                date_to=form.cleaned_data['data_until'],
                room=room,
                user=user,
            )

    context = {
        'room': room,
        'unbooked_dates': service.get_unbooked_days(room_id),
        'form': form,
        'info': info
    }

    return render(
        request,
        'room.html',
        context
    )
