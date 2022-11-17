from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    rating = models.IntegerField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

@receiver(post_save, sender=Project)
def make_project_cmplt(sender, instance, **kwargs):
    instance.completed = True
    print(instance.completed)
    instance.save()

