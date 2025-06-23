from django.db import models

class Tasks(models.Model):
    task = models.CharField(max_length=64)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}: {self.task} is {self.done}" 