from django.db import models
from django.contrib.auth import get_user_model


# Campaign = top-level initiative (Monkey King, Hiking for Health)
class Campaign(models.Model):
   name = models.CharField(max_length=200)
   description = models.TextField()
   start_date = models.DateField()
   end_date = models.DateField()
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.name
   
# Fundraiser = created by a participant (school, group, etc.)
class Fundraiser(models.Model):
   title = models.CharField(max_length=200)
   description = models.TextField()
   goal = models.IntegerField()
   image = models.URLField()
   is_open = models.BooleanField()
   date_created = models.DateTimeField(auto_now_add=True)

   owner = models.ForeignKey(
      get_user_model(), 
      related_name='owned_fundraisers', 
      on_delete=models.CASCADE
      )
   campaign = models.ForeignKey(
      'Campaign', 
      related_name='fundraisers', 
      on_delete=models.CASCADE
      )
   def __str__(self):
      return f"{self.title} ({self.campaign.name})"

# Pledge = donations from individuals (donors)
class Pledge(models.Model):   
   amount = models.IntegerField()
   comment = models.CharField(max_length=200)
   anonymous = models.BooleanField()

   fundraiser = models.ForeignKey(
      'Fundraiser', 
      related_name='pledges', 
      on_delete=models.CASCADE
      )
   
   supporter = models.ForeignKey(
      get_user_model(), 
      related_name='pledges', 
      on_delete=models.CASCADE
      )

   def __str__(self):
      return f"Pledge {self.amount} to {self.fundraiser}"
   

   # Sponsor = organizations who donate fixed/variable amounts
class Sponsor(models.Model):
   user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
   organization_name = models.CharField(max_length=200)
   contact_email = models.EmailField()

   def __str__(self):
      return self.organization_name