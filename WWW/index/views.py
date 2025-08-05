from django.shortcuts import render
from .models import TeamMember, Client, FinishedProject

def index(request):
    team = TeamMember.objects.all()[:3]  # przykładowo 3 osoby na landing page
    clients = Client.objects.all()[:6]   # przykładowo 6 klientów na landing page
    projects = FinishedProject.objects.order_by('-date_finished')[:3]  # 3 ostatnie realizacje
    return render(request, 'index/index.html', {
        'team': team,
        'clients': clients,
        'projects': projects,
    })

def team_list(request):
    team = TeamMember.objects.all()
    return render(request, 'index/team.html', {'team': team})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'index/clients.html', {'clients': clients})

def finished_projects(request):
    projects = FinishedProject.objects.order_by('-date_finished')
    return render(request, 'index/projects.html', {'projects': projects})
