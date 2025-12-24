from django.db import models

# Create your models here.
class Player(models.Model):
    pid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    age = models.IntegerField()
    height = models.FloatField()

class Stats(models.Model):
        player = models.ForeignKey(Player, on_delete=models.CASCADE , related_name='stats')
        position = models.CharField(max_length=100)
        team = models.CharField(max_length=100)
        goals = models.IntegerField()
        rating = models.FloatField()