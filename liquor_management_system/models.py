from django.db import models


class AadhaarInfo(models.Model):
    aadhaar_id = models.IntegerField(default=0)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)

    def __str__(self):
        return '{} {} {} {}'.format(self.aadhaar_id, self.first_name, self.last_name, self.age)


class State(models.Model):
    state_name = models.CharField(max_length=50)
    time_limit = models.FloatField(default=0.0)

    def __str__(self):
        return '{} {}'.format(self.state_name, self.time_limit)


class Liquor(models.Model):

    liquor_name = models.CharField(max_length=100, default='')
    liquor_quantity = models.FloatField(null=True, default=0)

    def __str__(self):
        return '{} {}'.format(self.liquor_name, self.liquor_quantity)


class Transaction(models.Model):
    aadhaar_info = models.ForeignKey(AadhaarInfo, on_delete=models.CASCADE)
    state_info = models.ForeignKey(State, on_delete=models.CASCADE)
    liquor_info = models.ForeignKey(Liquor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()

    def __str__(self):
        return '{} {} {}'.format(self.aadhaar_info, self.state_info, self.liquor_info, self.timestamp)
