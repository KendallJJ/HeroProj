# Generated by Django 3.2.8 on 2021-10-25 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('alter_ego', models.CharField(max_length=50)),
                ('primary_ability', models.CharField(max_length=50)),
                ('secondary_ability', models.CharField(max_length=50)),
                ('catch_phrase', models.CharField(max_length=50)),
            ],
        ),
    ]
