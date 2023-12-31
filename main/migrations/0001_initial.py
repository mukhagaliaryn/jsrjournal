# Generated by Django 4.2 on 2023-08-31 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='ФИО контактного лица')),
                ('email', models.EmailField(max_length=254, verbose_name='Email контактного лица')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон контактного лица')),
                ('category', models.CharField(choices=[('1', 'Педагогические науки'), ('2', 'Искусство и гуманитарные науки'), ('3', 'Социальные науки, журналистика и информация'), ('4', 'Бизнес, управление и право'), ('5', 'Естественные науки, математика и статистика'), ('6', 'Информационно-коммуникационные технологии'), ('7', 'Инженерные, обрабатывающие и строительные отрасли'), ('8', 'Сельское хозяйство и биоресурсы'), ('9', 'Ветеринария'), ('10', 'Здравоохранение'), ('11', 'Услуги'), ('12', 'Национальная безопасность и военное дело')], default='Педагогические науки', max_length=255, verbose_name='Научное направление')),
                ('item', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10)], default=1, max_length=20, verbose_name='Количество необходимых печатных экземпляров')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
