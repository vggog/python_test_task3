from django.db.models.query import QuerySet

from .models import Room


class Service:

    def get_all_rooms(self):
        return Room.objects.all()

    @staticmethod
    def get_sorting_rooms(
            value_from_form: str,
            is_ascending: bool = True
    ):
        """Метод для получения отсортированных данных"""
        column = value_from_form if is_ascending else f'-{value_from_form}'
        return Room.objects.order_by(column)

    def _get_rooms_with_sorting(self, sorting_value: str, rooms: QuerySet):
        """Метод для получения отсортированных данных по нужным критериям"""
        if sorting_value == 'price_up':
            return rooms.order_by('price')
        elif sorting_value == 'price_down':
            return rooms.order_by('-price')
        elif sorting_value == 'seats_up':
            return rooms.order_by('num_of_seats')
        elif sorting_value == 'seats_down':
            return rooms.order_by('-num_of_seats')

        return rooms.all()

    def get_rooms_with_sorting_and_filtering(self, form):
        """Возвращает комнаты по нужным критериям"""
        price_filter_from = form.cleaned_data['price_from']
        price_filter_up_to = form.cleaned_data['price_up_to']

        seats_filter_from = form.cleaned_data['num_of_seats_from']
        seats_filter_up_to = form.cleaned_data['num_of_seats_up_to']

        rooms = Room.objects

        if price_filter_from:
            rooms = rooms.filter(price__gte=price_filter_from)

        if price_filter_up_to:
            rooms = rooms.filter(price__lte=price_filter_up_to)

        if seats_filter_from:
            rooms = rooms.filter(num_of_seats__gte=seats_filter_from)

        if seats_filter_up_to:
            rooms = rooms.filter(num_of_seats__lte=seats_filter_up_to)

        sorting = form.cleaned_data['sort']

        return self._get_rooms_with_sorting(sorting_value=sorting, rooms=rooms)
