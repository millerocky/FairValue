# Generated by Django 4.0.3 on 2022-05-02 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_delete_stocks_remove_stocksy_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocksy',
            name='sector',
        ),
    ]
