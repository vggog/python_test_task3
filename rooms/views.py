from django.shortcuts import render
from django.http import HttpResponse


def all_rooms(request) -> HttpResponse:
    return HttpResponse("all rooms page")
