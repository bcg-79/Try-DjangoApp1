from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ExpAccounts(models.Model):
    acc_name = models.CharField('Account Name', max_length=100)
    #acc_type = models.CharField(max_length=100)  # Personal, Commercial, or any other type...
    acc_type = models.CharField(max_length=60, choices=[('personal', 'Personal'), ('commercial', 'Commercial'), ('other', 'Other')])
    initial_amount = models.FloatField(default=0.0)
    rem_amount = models.FloatField(default=0.0)
    status = models.IntegerField(default=0)
    date_created = models.DateField(default=timezone.now)
    user_acc = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.acc_name      #self.status

class ExpTransactions(models.Model):
    person_name = models.CharField(max_length=100)
    amount = models.FloatField()
    category = models.CharField(max_length=100, choices=[('food', 'Food'), ('hospital', 'Hospital'), ('other', 'Other')])
    date_time = models.DateField(default=timezone.now)
    add_spend = models.IntegerField(choices=[(0, 'Spend'), (1, 'Add')]) # 0 -> spend, 1 -> add
    extra_note = models.TextField()
    exp_acc = models.ForeignKey(ExpAccounts, on_delete=models.CASCADE)

    def __str__(self):
        return self.person_name
