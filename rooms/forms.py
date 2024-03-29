from django import forms


class FilterAndSortForm(forms.Form):
    SORT = [
        ('None', 'Нет'),
        ('price_up', 'Цена по возрастанию'),
        ('price_down', 'Цена по убыванию'),
        ('seats_up', 'Количество мест по возрастанию'),
        ('seats_down', 'Количество мест по убыванию'),
    ]

    sort = forms.ChoiceField(
        label='Сортировать',
        widget=forms.Select,
        choices=SORT,
    )
