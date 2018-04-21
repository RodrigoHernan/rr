from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_Cliente(sender, instance, created, **kwargs):
    try:
        if created:
            Cliente.objects.create(user=instance)
        instance.cliente.save()
    except Exception as uid:
        print(uid)
        print('si tenes un super user lo tenes que crear de nuevo')
