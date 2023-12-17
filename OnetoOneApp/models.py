from django.db import models

# Create your models here.
class Brain(models.Model):
    iq = models.IntegerField()
    wieght = models.IntegerField()

class Human(models.Model):
    SEX = (
        ('male', 'мужской'),
        ('female', 'женский'),
        ('think', 'неопределенный'),
        ('fight helicopter', 'боевой вертолетик')
    )
    name = models.CharField(max_length=50, default='john') 
    sex = models.CharField(max_length=20, choices=SEX)
    brain = models.OneToOneField(
        Brain,
        on_delete=models.CASCADE,
        related_name='human' 
    )


# brain1 = Brain.objects.create(iq=110, wieght=2)
# human1 = Human.objects.create(sex='male', brain=brain1)
# human1.brain
# <Brain: Brain object (1)>
# brain1.human
# <Human: Human object (1)>