# Generated by Django 4.0.3 on 2022-05-01 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_stocksy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Stocks',
        ),
        migrations.RemoveField(
            model_name='stocksy',
            name='position',
        ),
    ]
