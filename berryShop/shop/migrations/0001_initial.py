# Generated by Django 3.2.8 on 2021-10-19 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(default='0', unique=True, verbose_name='Страница')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Клубника', max_length=10, verbose_name='Название')),
                ('text', models.TextField(default='Текст', max_length=2000, verbose_name='Описание')),
                ('number', models.SmallIntegerField(default='1', verbose_name='Кол-во в коробке')),
                ('image_1', models.ImageField(default=None, upload_to='', verbose_name='Изображение 1')),
                ('image_2', models.ImageField(default=None, upload_to='', verbose_name='Изображение 2')),
                ('price', models.SmallIntegerField(default='1600', verbose_name='Цена')),
                ('discount', models.SmallIntegerField(default='0', verbose_name='Скидка')),
                ('slug', models.SlugField(default='0', unique=True, verbose_name='Страница')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
    ]
