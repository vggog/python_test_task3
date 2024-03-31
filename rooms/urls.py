from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_rooms),
    path('<int:room_id>', views.get_room, name='room')
]
