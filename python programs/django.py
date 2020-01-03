from django.db import models
from django.utls.encoding import python_2_unicode_compatible

@python_2_unicode_compatible  #for python 3.5+ and 2.7
class iceCreamBar(models.model):
    name = models.charField(max_length=100)
    shell = models.charField(max_length=100)
    filling = models.charField(max_length=100)
    has_stick = models.BooleanField(default=True)

    def __str__(self):
        return self.name
