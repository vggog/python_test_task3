from .models import Room
from .forms import FilterAndSortForm


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

    def get_rooms_with_sorting(self, form: FilterAndSortForm):
        """Метод для получения отсортированных данных по нужным критериям"""
        sorting = form.cleaned_data['sort']
        if sorting == 'price_up':
            return self.get_sorting_rooms('price')
        elif sorting == 'price_down':
            return self.get_sorting_rooms('price', False)
        elif sorting == 'seats_up':
            return self.get_sorting_rooms('num_of_seats')
        elif sorting == 'seats_down':
            return self.get_sorting_rooms('num_of_seats', False)
        else:
            return self.get_all_rooms()
