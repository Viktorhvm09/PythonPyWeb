# Generated by Django 4.2.5 on 2025-03-31 20:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_train', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(blank=True, help_text='Напишите здесь о том, почему Вы так хороши', null=True, verbose_name='Биография'),
        ),
        migrations.AlterField(
            model_name='author',
            name='city',
            field=models.CharField(blank=True, help_text='Введите название города', max_length=100, null=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_birth',
            field=models.DateField(blank=True, help_text='Посланцев из будущего не регистрируем!', null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(help_text='Адрес почты в формате *@*.*', max_length=254, unique=True, verbose_name='Адрес электронной почты'),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(blank=True, help_text='Ограничение - не более 100 символов', max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='author',
            name='gender',
            field=models.CharField(blank=True, choices=[('м', 'мужской'), ('ж', 'женский')], help_text='Выберите пол', max_length=1, null=True, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, help_text='Фото в профиль, можно не своё! Ну или хоть какое-то. Ладно можно без фото', null=True, upload_to='foto_profile', verbose_name='Картинка профиля'),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(blank=True, help_text='Ограничение - не более 100 символов', max_length=100, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='author',
            name='middle_name',
            field=models.CharField(blank=True, help_text='Ограничение - не более 100 символов', max_length=100, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='author',
            name='phone_number',
            field=models.CharField(blank=True, help_text="Введите номер телефона через '+7' без пробелов в формате +79123456789 ", max_length=12, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Телефонный номер должен быть формата: '+79123456789'.", regex='^\\+79\\d{9}$')], verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='author',
            name='self_esteem',
            field=models.DecimalField(blank=True, decimal_places=1, help_text="Введите уровень вашей самооценки, только честно! Градация от 0 до 5, где 0 - 'я молодец', 5 - 'я умница'", max_digits=2, null=True, validators=[django.core.validators.MinValueValidator(0, 'Диапазон [0.0, 5.0]'), django.core.validators.MaxValueValidator(5, 'Диапазон [0.0, 5.0]')], verbose_name='Уровень самооценки'),
        ),
        migrations.AlterField(
            model_name='author',
            name='status_rule',
            field=models.BooleanField(help_text='А ты их читал или как обычно просто галочку поставил?', verbose_name='Согласие с правилами'),
        ),
        migrations.AlterField(
            model_name='author',
            name='username',
            field=models.SlugField(help_text="Введите username, не длиннее 50 символов. Использовать нужно английский алфавит, разделять фразы нужно символом '-'", unique=True, verbose_name='Имя аккаунта'),
        ),
    ]
