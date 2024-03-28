from django.db import models


class Room(models.Model):
    title = models.CharField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    num_of_seats = models.IntegerField()


class BookingRecords(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
