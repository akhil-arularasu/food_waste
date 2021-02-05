from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class CountryLevelWaste(models.Model):
    name = models.CharField(max_length=200,unique=True)
    gdp = models.IntegerField(default=0)
    total_waste = models.IntegerField(default=0)
    organic_pct = models.FloatField(default=0.0)
    population = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("foodwaste:country_detail",kwargs={'pk':self.pk})

    @property
    def waste_per_person(self):
       return round((self.total_waste * 2000) / (self.population * 365),2)

    @property
    def organic_waste_per_person(self):
        return round((self.total_waste *
        self.organic_pct/100 * 2000) / (self.population * 365),2)

# Create your models here.
class PledgeInfo(models.Model):
    email = models.EmailField(max_length=254,blank=True, default='')
    zip_code = models.IntegerField(null=True, validators=[
                MinValueValidator(1)])
    city = models.CharField(max_length=128,blank=True, default='')
    state = models.CharField(max_length=128,blank=True, default='')
    country = models.CharField(max_length=128,blank=True, default='')
#    account = models.IntegerField(unique=True)
#    city = models.CharField(max_length=200,default="")
    total_waste_per_week = models.IntegerField(default=1, validators=[
                MaxValueValidator(100),
                MinValueValidator(1)])
    total_food_waste_per_week = models.IntegerField(default=1, validators=[
                MaxValueValidator(100),
                MinValueValidator(1)])
    pledged_reduction = models.IntegerField(default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)]
    )
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'pledge'

    # class Meta:
    #     ordering = ["-created_at"]
    #     unique_together = [first_name"", "last_name"]

# Create your models here.
