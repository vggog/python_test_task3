from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .service import Service
from .forms import FilterAndSortForm


def all_rooms(request: HttpRequest) -> HttpResponse:
    service = Service()

    if request.method == 'POST':
        form = FilterAndSortForm(request.POST)
        if form.is_valid():
            rooms = service.get_rooms_with_sorting(form)
        else:
            return HttpResponse('Не валидная форма')
    else:
        rooms = service.get_all_rooms()
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
