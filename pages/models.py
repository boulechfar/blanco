from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save 
from django.dispatch import receiver
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number= models.CharField(max_length=10)
    address=models.CharField(max_length=200)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created , **kwargs):
    if created:
        Profile.objects.create(
            user=instance

        )        
        
        

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
        

