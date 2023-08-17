# Generated by Django 4.2.4 on 2023-08-16 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Событие')),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='is_courier',
            field=models.BooleanField(default=False, verbose_name='Курьер'),
        ),
        migrations.AlterField(
            model_name='client',
            name='is_florist',
            field=models.BooleanField(default=False, verbose_name='Флорист'),
        ),
    ]