from django.db import models

class UserData(models.Model):
    full_name = models.CharField('Full name', max_length=200)
    email = models.CharField('Email', max_length=200)
    adress = models.CharField('Adress', max_length=200)
    phone_number = models.CharField('Phone', max_length=200)
    current_balance = models.FloatField('Balance')
    last_payment = models.DateTimeField('Last_payment')
    reg_date = models.DateTimeField('Reg_date')  
    lastcall_date = models.DateTimeField('Lastcall date')
    status = models.BooleanField('Status')  


    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'