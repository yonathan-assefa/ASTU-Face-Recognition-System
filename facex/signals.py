from django.dispatch import receiver
from django.db.models.signals import post_delete, post_init, post_save


from users_app.models import UserProfile
from facex.models import Student


# Studnet Profile File Control
@receiver(post_delete, sender=Student)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) 


@receiver(post_init, sender= Student)
def backup_image_path(sender, instance, **kwargs):
    instance._current_imagen_file = instance.image


@receiver(post_save, sender= Student)
def delete_old_image(sender, instance, **kwargs):
    if hasattr(instance, '_current_imagen_file'):
        if instance._current_imagen_file != instance.image.path:
            instance._current_imagen_file.delete(save=False)


class StudentLog(models.Model):
	log_history = models.FileField(upload_to = 'media/logs/%y/%m')
	log_date = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.log_date.__str__()




#User profile File Control
@receiver(post_delete, sender=UserProfile)
def submission_delete(sender, instance, **kwargs):
    instance.profile_picture.delete(False) 


@receiver(post_init, sender= UserProfile)
def backup_image_path(sender, instance, **kwargs):	
	instance._current_imagen_file = instance.profile_picture


@receiver(post_save, sender= UserProfile)
def delete_old_image(sender, instance, **kwargs):
    if hasattr(instance, '_current_imagen_file'):
        if instance._current_imagen_file != instance.profile_picture.path:
            instance._current_imagen_file.delete(save=False)