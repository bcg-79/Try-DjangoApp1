# Generated by Django 4.0 on 2022-01-04 09:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_name', models.CharField(max_length=100, verbose_name='Account Name')),
                ('acc_type', models.CharField(choices=[('personal', 'Personal'), ('commercial', 'Commercial'), ('other', 'Other')], max_length=60)),
                ('initial_amount', models.FloatField(default=0.0)),
                ('rem_amount', models.FloatField(default=0.0)),
                ('status', models.IntegerField(default=0)),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ExpTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('category', models.CharField(choices=[('food', 'Food'), ('hospital', 'Hospital'), ('other', 'Other')], max_length=100)),
                ('date_time', models.DateField(default=django.utils.timezone.now)),
                ('add_spend', models.IntegerField(choices=[(0, 'Spend'), (1, 'Add')])),
                ('exp_acc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.expaccounts')),
            ],
        ),
    ]
