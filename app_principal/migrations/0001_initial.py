# Generated by Django 3.1.3 on 2020-11-06 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='informacion_personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('nacimiento', models.CharField(max_length=50)),
                ('nacionalidad', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=15)),
                ('cuidad', models.CharField(max_length=50)),
                ('edad', models.CharField(max_length=5)),
                ('cargo_actual', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
