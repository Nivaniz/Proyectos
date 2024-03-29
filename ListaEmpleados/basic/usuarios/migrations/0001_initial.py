# Generated by Django 4.2.1 on 2023-06-09 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expediente', models.IntegerField()),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('nombre', models.CharField(max_length=100)),
                ('profesion', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
            ],
        ),
    ]
