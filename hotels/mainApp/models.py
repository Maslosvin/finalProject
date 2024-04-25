from django.db import models

# Модель для представления отдельной комнаты в отеле
class Room(models.Model):
    id = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=100)  # Название отеля
    room_number = models.CharField(max_length=10)  # Номер комнаты
    capacity = models.TextField()  # Вместимость комнаты
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена за проживание
    rating = models.DecimalField(max_digits=3, decimal_places=2)  # Рейтинг комнаты

# Модель для хранения информации о бронировании комнаты
class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # Связь с комнатой
    check_in_date = models.DateField()  # Дата заезда
    check_out_date = models.DateField()  # Дата выезда
    guest_count = models.IntegerField()  # Количество гостей
    services = models.TextField()  # Дополнительные услуги
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Общая цена бронирования

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