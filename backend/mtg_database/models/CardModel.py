from django.db import models


class Cost(models.Model):
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


class Type(models.Model):
    cards = models.ManyToManyField(Card, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Creature(Type):
    power = models.IntegerField()
    toughness = models.IntegerField()


class SubType(models.Model):
    cards = models.ManyToManyField(Card, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Ability(models.Model):
    cards = models.ManyToManyField(Card, on_delete=models.CASCADE)
    effect = models.CharField(max_length=300)


class ActivatedAbility(Ability):
    cost = models.ForeignKey(Cost, on_delete=models.CASCADE)

