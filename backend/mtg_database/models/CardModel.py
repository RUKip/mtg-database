from django.db import models

class Cost():
    colorless = models.IntegerField(default=0)
    red = models.IntegerField(default=0)
    blue = models.IntegerField(default=0)
    green = models.IntegerField(default=0)
    black = models.IntegerField(default=0)
    white = models.IntegerField(default=0)
    life = models.IntegerField(default=0)

class Card(models.Model):
    name = models.CharField(max_length=50)
    cost = models.ForeignKey(Cost, on_delete=models.CASCADE)

class Types():
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    type_id = models.BigIntegerField()

class SubTypes():
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    sub_type_id = models.BigIntegerField()
