from django.db import models



class CharityFund(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def total(self):
        return sum(d.amount for d in self.donation_set.all())


class Donation(models.Model):
    charity_fund = models.ForeignKey(CharityFund)
    name = models.CharField(max_length=200)
    amount = models.IntegerField()
    public = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
