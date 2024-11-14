from django.db import models

# Create your models here.

class position(models.Model):
    title=models.CharField(max_length=50)


class Client(models.Model):
    fullname=models.CharField(max_length=100)
    File_no=models.CharField(max_length=10,default='BMD000')
    Clicode=models.CharField(max_length=10)
    position=models.ForeignKey(position,on_delete=models.CASCADE)
    case_no=models.CharField(max_length=10,primary_key=True,default='BMB000')
    other_parties=models.CharField(max_length=100,null=True)
    other_partiesreps=models.CharField(max_length=100,null=True)



class Case(models.Model):
    case_type=models.CharField(max_length=100)
    case_no = models.ForeignKey(Client, on_delete=models.CASCADE)
    filed_date=models.CharField(max_length=20)
    status=models.CharField(max_length=100)
    matter_coming_up=models.CharField(max_length=100,null=True)
    Advocate_assigned=models.CharField(max_length=100,null=True)
    
   
class Party(models.Model):
    fullname=models.CharField(max_length=100)   
    party_type=models.CharField(max_length=100)  

class Hearing(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)  
    hearing_date = models.DateField()
    outcome = models.TextField()
    presiding=models.TextField()
    court=models.TextField()

class Ruling(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)  
    ruling_date = models.DateField()
    ruling_summary = models.TextField()  

class Payment(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)  # Foreign key linking to Case
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    balance_remaining = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()      