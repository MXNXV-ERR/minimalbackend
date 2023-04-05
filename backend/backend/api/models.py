from django.db import models

# Create your models here.

class Predictions(models.Model):
    review = models.CharField(max_length=1000)
    pred = models.BooleanField()
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return '{self.review} - {self.pred}'
