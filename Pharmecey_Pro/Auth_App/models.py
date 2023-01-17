from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    addess = models.CharField(max_length=160, null=True)
    dob = models.DateField(null=True)
    phone = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(upload_to='profile_img', null=True)


    def __str__(self) -> str:
        return str(self.user)

@receiver(post_save, sender=User)
def create_or_save(sender, created, instance, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    # instance.profile.save()
        
