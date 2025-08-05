from django.db import models

# Create your models here.

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team_photos/')
    description = models.TextField(blank=True)
    education = models.CharField(max_length=200, blank=True)
    role = models.CharField(max_length=100)
    interests = models.CharField(max_length=200, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

class Ad(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ads/')
    url = models.URLField(blank=True)
    client_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Client(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='client_logos/', blank=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

class FinishedProject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='portfolio/', blank=True)
    date_finished = models.DateField(null=True, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
