from django.db import models

class Entrepreneur(models.Model):
    name = models.CharField(max_length=200)
    email=models.EmailField(max_length=100)
    ideas = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name

   
   
class Funders(models.Model):
    name = models.CharField(max_length=100)
    ename = models.CharField(max_length=100)
    E_ideas = models.TextField()
    amount = models.IntegerField()

    def __str__(self):
        return self.name
      
#for donation
class Donaters(models.Model):
    Funder = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    amount = models.IntegerField()

    def __str__(self):
        return self.Funder
    


class Innovaters(models.Model):
    fk = models.ForeignKey(Entrepreneur,on_delete=models.CASCADE)
    @property
    def name(self):
        return self.fk.name

