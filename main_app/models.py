from django.db import models
from django.urls import reverse

class Birdhouse(models.Model):
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f'A {self.size} {self.color} birdhouse'
    
    def get_absolute_url(self):
        return reverse('birdhouses_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    age = models.IntegerField()
    birdhouses = models.ManyToManyField(Birdhouse)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('details', kwargs={'finch_id': self.id})
   
class Feeding(models.Model):
    MEALS = (
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner'),
    )
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'
    
    class Meta:
        ordering = ['-date']