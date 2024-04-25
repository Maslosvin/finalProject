from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Room, Reservation, Booking, Notification
from .forms import ReservationForm

# Перенаправление на страницу hotels-main в случае попадения на страницу с отсутствующим доменом
def redirect_to_main(request):
    return redirect("hotels-main")

# Регистрация с последующим перенаправлением на логин
def register(request):
    from django.contrib import messages
    from mainApp.forms import UserRegisterForm
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Вы успешно зарегистрировались")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration.html', {"reg_form": form})

def main_page_view(request):
    # Получаем все комнаты
    rooms = Room.objects.all()

    # Получаем последние бронирования
    bookings = Booking.objects.order_by('-booking_date')[:5]

    context = {
        'rooms': rooms,
        'bookings': bookings,
    }

    return render(request, 'mainPage.html', context)


def calculate_total_price(room, check_in_date, check_out_date, guest_count):
    # Здесь проводите расчет итоговой цены, например, на основе цены за номер, количества дней проживания и количества гостей
    total_price = room.price_per_night * (check_out_date - check_in_date).days * guest_count
    return total_price


def reserve_hotel_view(request):
    message = ""
    context = {}

    if request.method == 'POST':
        search_query = request.POST.get('search_query')

        if search_query != "":
            hotels = Room.objects.filter(hotel_name__icontains=search_query)
            context = {'hotels': hotels, 'search_query': search_query, 'message': message}

        form = ReservationForm(request.POST)
        if form.is_valid():
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            guest_count = form.cleaned_data['guest_count']

            # Save reservation to the database
            reservation = Reservation(room=Room, check_in_date=check_in_date, check_out_date=check_out_date,
                                      guest_count=guest_count)
            reservation.save()

            context['form'] = form


    else:
        form = ReservationForm()
        context = {'form': form, 'message': message, }

    return render(request, 'reserveHotel.html', context)

def payment_view(request):
        pass