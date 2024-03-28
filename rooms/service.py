from .models import Room


class Service:

    def get_all_rooms(self):
        return Room.objects.all()
