from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Room, Reservation, Booking, Notification, User
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

# цена = цена отеля за день * на (дата выезда - дата въезда) * на кол-во гостей
def calculate_total_price(room, check_in_date, check_out_date, guest_count):
    total_price = room.price * (check_out_date - check_in_date).days * guest_count
    return total_price


def reserve_hotel_view(request):
    message = ""
    context = {}
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        form = ReservationForm(request.POST)

        if form.is_valid():
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            guest_count = form.cleaned_data['guest_count']

            if search_query:
                hotels = Room.objects.filter(hotel_name__icontains=search_query)
                if hotels.exists():
                    room = hotels.first()
                    total_price = calculate_total_price(room, check_in_date, check_out_date, guest_count)
                    context = {'form': form, 'hotels': hotels, 'search_query': search_query, 'totalprice': total_price}
                else:
                    message = "Не удалось найти отель с таким именем."
                    context = {'form': form, 'message': message}
            else:
                message = "Выберите отель для продолжения."
                context = {'form': form, 'message': message}
        else:
            message = "Форма заполнена неверно. Пожалуйста, исправьте ошибки."
            context = {'form': form, 'message': message}
    else:
        form = ReservationForm()
        context = {'form': form, 'message': message}

    return render(request, 'reserveHotel.html', context)


def profile_view(request):
    if request.user.is_authenticated:  # Проверяем, авторизован ли пользователь
        user_id = request.user.id

        # Получаем данные о госте и его бронированиях
        user = User.objects.get(user_id=user_id)
        bookings = Booking.objects.filter(user=user)

        context = {
            'full_name': user.full_name,  # Имя пользователя
            'bookings': bookings,  # Список бронированных отелей
        }
        return render(request, 'profilePage.html', context)
    else:
        return redirect('login')  # В случае если пользователь не авторизован, перенаправляем на страницу входа

def payment_view(request):
    return render(request, 'paymentPage.html')