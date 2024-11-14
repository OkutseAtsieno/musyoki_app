
from django.db import models

from django.contrib.auth import get_user_model


    
    # CourtEvent model (placeholder)
class CourtEvent(models.Model):
    pass

# Case model (placeholder)
class Case(models.Model):
    pass    

class Advocate(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)