# Generated by Django 4.0.4 on 2022-05-01 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=1000)),
                ('picture', models.ImageField(upload_to='images')),
                ('name', models.CharField(max_length=20)),
                ('symbol', models.CharField(max_length=10)),
                ('sector', models.CharField(max_length=50)),
            ],
        ),
    ]
