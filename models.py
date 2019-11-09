from django.db import models


class Continent(models.Model):
    class Meta:
        verbose_name_plural = "Continents"

    name = models.TextField()

    def __str__(self): return self.name

    # TODO: implement __str__ method


class Brand(models.Model):
    CHOICES = (
        ('c', 'Cabriolet'),
        ('s', 'SUV')
    )

    name = models.TextField()
    type = models.CharField(max_length=1, choices=CHOICES)
    release_date = models.DateField()
    plot = models.TextField()
    lifetime = models.PositiveIntegerField(help_text="in Years")
    black_and_white = models.BooleanField()
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    gearbox = models.ManyToManyField('Car')

    def __str__(self): return self.name

    # TODO: implement __str__ method


class CarManager(models.Manager):

    def duplicates(self):
        # TODO: implement an algorithm to find duplicate entries
        return []


class Car(models.Model):
    gearbox = models.TextField()

    objects = CarManager()

    def __str__(self): return self.gearbox

    # TODO: implement __str__ method
