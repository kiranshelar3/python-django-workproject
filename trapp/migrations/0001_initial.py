# Generated by Django 3.2.7 on 2021-09-15 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dmdl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=15)),
                ('phoneno', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]
