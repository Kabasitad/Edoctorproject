# Generated by Django 4.1.5 on 2023-01-28 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='checkin',
        ),
        migrations.RemoveField(
            model_name='orderloan',
            name='checkin',
        ),
        migrations.DeleteModel(
            name='Checkin',
        ),
        migrations.DeleteModel(
            name='Medicine',
        ),
        migrations.DeleteModel(
            name='OrderLoan',
        ),
    ]