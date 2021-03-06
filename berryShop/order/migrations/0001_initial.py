# Generated by Django 3.2.8 on 2021-11-02 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_order', models.SmallIntegerField(verbose_name='Номер заказа')),
                ('name_user', models.CharField(max_length=15, verbose_name='Имя')),
                ('last_name_user', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('address', models.CharField(max_length=50, verbose_name='Адресс доставки')),
                ('phone', models.SmallIntegerField(verbose_name='Телефон')),
                ('text', models.TextField(max_length=400, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
