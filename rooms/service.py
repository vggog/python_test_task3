from _datetime import date, timedelta
from typing import Iterator

from django.db.models.query import QuerySet
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from .models import Room, BookingRecords


class Service:

    def get_all_rooms(self):
        return Room.objects.all()

    def get_room(self, room_id: int) -> Room | None:
        """Вернуть комнату или None если комната не найдена"""
        try:
            return Room.objects.get(id=room_id)
        except ObjectDoesNotExist:
            return None

    def get_unbooked_days(self, room_id: int) -> map:
        """Получить представление не забронированных дат в формате строки"""
        unbooked_days = self.get_unbooked_days_data_format(room_id)

        return map(lambda d: d.strftime('%B %d, %Y'), unbooked_days)

    def get_unbooked_days_data_format(self, room_id: int) -> list[date]:
        """Получить не забронированные даты"""
        current_date = date.today()
        next_date = current_date + timedelta(days=15)

        dates = []
        for d in self.date_generator(current_date, next_date):
            booking_day = (
                BookingRecords.objects
                .filter(id=room_id)
                .filter(
                    (
                        Q(date_from__lte=d)
                        & Q(date_to__gte=d)
                    )
                )
            )

            if booking_day:
                continue

            dates.append(d)

        return dates

    @staticmethod
    def date_generator(start_date: date, end_date: date) -> Iterator[date]:
        """Генератор дат в промежутке от start_date до end_date"""
        for n in range(int((end_date - start_date).days) + 1):
            yield start_date + timedelta(n)

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
