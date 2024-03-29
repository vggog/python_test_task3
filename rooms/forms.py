from django import forms


class FilterAndSortForm(forms.Form):
    SORT = [
        ('None', 'Нет'),
        ('price_up', 'Цена по возрастанию'),
        ('price_down', 'Цена по убыванию'),
        ('seats_up', 'Количество мест по возрастанию'),
        ('seats_down', 'Количество мест по убыванию'),
    ]

    price_from = forms.CharField(
        label='Цена от',
        widget=forms.NumberInput,
        required=False
    )
    price_up_to = forms.CharField(
        label='Цена до',
        widget=forms.NumberInput,
        required=False
    )

    num_of_seats_from = forms.CharField(
        label='Количество мест от',
        widget=forms.NumberInput,
        required=False
    )
    num_of_seats_up_to = forms.CharField(
        label='Количество мест до',
        widget=forms.NumberInput,
        required=False
    )

    sort = forms.ChoiceField(
        label='Сортировать',
        widget=forms.Select,
        choices=SORT,
    )
