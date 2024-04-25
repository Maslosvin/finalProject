from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Room, Reservation, Booking, Notification

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




def reserve_hotel_view(request):
    message = ""
    context = {}
    if request.method == 'POST':
        search_query = request.POST.get('search_query')  # Получаем поисковый запрос из формы
        if search_query != "":
            # Ищем отели в базе данных по введенному названию
            hotels = Room.objects.filter(hotel_name__icontains=search_query)
            context = {'hotels': hotels, 'search_query': search_query, 'message': message}
    return render(request, 'reserveHotel.html', context)