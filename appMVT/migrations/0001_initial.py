# Generated by Django 4.1.2 on 2022-11-06 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pariente', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('fecha_nac', models.DateField()),
            ],
        ),
    ]