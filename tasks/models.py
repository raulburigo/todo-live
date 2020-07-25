from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Task(models.Model):

    STATUS = (
        (1, 'Doing'),
        (2, 'Done'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    done = models.IntegerField(choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __repr__(self) -> str:
        return f'<{type(self).__name__} title={self.title!r} created at= day {self.created_at.day!r} hour {self.created_at.hour!r}>'