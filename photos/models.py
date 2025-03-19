from django.db import models

def upload_to(instance, filename):
    return f'events/{instance.event_id}/{filename}'

class Photo(models.Model):
    event_id = models.CharField(max_length=255)  # Identifiant de l'événement
    image = models.ImageField(upload_to=upload_to)
    score = models.FloatField(default=0.0)
