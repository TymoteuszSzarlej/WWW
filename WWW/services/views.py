from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Service
from django.core.mail import send_mail
from django.conf import settings

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/list.html', {'services': services})

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'services/detail.html', {'service': service})

def free_valuation(request, pk):
    service = get_object_or_404(Service, pk=pk)
    valuation = None
    if request.method == 'POST':
        # Przykład: automatyczna wycena na podstawie współczynnika wyceny
        try:
            coeff = float(request.POST.get('valuation_coeff', service.valuation_coeff or 1))
            base_price = float(request.POST.get('base_price', service.price_min))
            valuation = base_price * coeff
            messages.success(request, f"Szacowana wycena: {valuation} zł")
        except Exception:
            messages.error(request, "Błąd podczas wyceny.")
    return render(request, 'services/free_valuation.html', {'service': service, 'valuation': valuation})

def schedule_meeting(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        details = request.POST.get('details')
        # Wyślij e-mail do zespołu lub zapisz zgłoszenie
        send_mail(
            subject=f"Nowe zapytanie o usługę: {service.name}",
            message=f"Imię i nazwisko: {name}\nEmail: {email}\nSzczegóły projektu: {details}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
        )
        messages.success(request, "Rozmowa została umówiona. Skontaktujemy się z Tobą wkrótce.")
        return redirect('service_detail', pk=pk)
    return render(request, 'services/schedule_meeting.html', {'service': service})
