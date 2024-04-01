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
    data_from = forms.DateField(
        label='Дата от',
        required=False,
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )
    data_until = forms.DateField(
        label='Дата до',
        required=False,
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    sort = forms.ChoiceField(
        label='Сортировать',
        widget=forms.Select,
        choices=SORT,
    )

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data['data_from'] and not cleaned_data['data_until']:
            raise forms.ValidationError(
                '"Дата до" также должно быть заполнена'
            )
        elif not cleaned_data['data_from'] and cleaned_data['data_until']:
            raise forms.ValidationError(
                '"Дата от" также должно быть заполнена'
            )

        if cleaned_data['data_from'] and cleaned_data['data_until']:
            if cleaned_data['data_from'] > cleaned_data['data_until']:
                raise forms.ValidationError(
                    '"Дата от" должен быть больше чем "Дата до"'
                )

        return cleaned_data
