from django.db import models


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guest_count = models.IntegerField()
    services = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

# Модель для хранения информации о госте
class Guest(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)  # Полное имя
    email = models.EmailField()  # Email гостя
    phone = models.CharField(max_length=20)  # Номер телефона

# Модель для связи гостя с бронировкой комнаты
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)  # Связь с гостем
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)  # Связь с бронировкой
    additional_services = models.TextField()  # Дополнительные услуги
    payment_status = models.CharField(max_length=20)  # Статус оплаты
    booking_date = models.DateTimeField(auto_now_add=True)  # Дата бронирования

# Модель для хранения уведомлений связанных с бронировкой
class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)  # Связь с бронировкой
    message = models.TextField()  # Текст уведомления
    timestamp = models.DateTimeField(auto_now_add=True)  # Дата создания уведомления