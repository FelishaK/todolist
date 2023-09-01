from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=250)
    complete = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
