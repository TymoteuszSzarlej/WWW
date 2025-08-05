from django.db import models

# Create your models here.
class Subscription(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    plan = models.CharField(max_length=100)
    max_users = models.IntegerField(default=1)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.plan
