from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_rooms),
    path('<int:room_id>', views.get_room, name='room'),
    path('booked_dates/', views.get_booking_records, name='booked_dates'),
    path(
        'booked_dates/delete/<int:booked_record_id>',
        views.delete_booked_required,
        name='delete_booked_dates',
    )
]
