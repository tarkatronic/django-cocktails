from django.db import models


class Ingredient(models.Model):
    OUNCE = 'ounce'
    TEASPOON = 'tsp'
    TABLESPOON = 'tbsp'
    DASH = 'dash'

    MEASUREMENTS = (
        (OUNCE, 'Ounce(s)'),
        (TEASPOON, 'Teaspoon(s)'),
        (TABLESPOON, 'Tablespoon(s)'),
        (DASH, 'Dash(es)'),
    )
    name = models.CharField(max_length=255)
    measurement = models.CharField(max_length=5, choices=MEASUREMENTS, null=True, blank=True)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=255)
    components = models.ManyToManyField('Ingredient', through='Component', related_name='drinks')

    def __str__(self):
        return self.name


class Component(models.Model):
    drink = models.ForeignKey('recipes.Drink', related_name='+')
    ingredient = models.ForeignKey('recipes.Ingredient', related_name='+')
    amount = models.FloatField()

    def __str__(self):
        return '%s %s %s (%s)' % (self.ingredient.name, self.amount, self.ingredient.get_measurement_display() or '', self.drink.name)


class Step(models.Model):
    drink = models.ForeignKey('Drink', related_name='steps')
    text = models.TextField()

    class Meta:
        order_with_respect_to = 'drink'

    def __str__(self):
        return '%s step #%s' % (self.drink.name, self._order + 1)
