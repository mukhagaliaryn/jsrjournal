# Generated by Django 4.2 on 2023-08-31 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='main/poster/', verbose_name='Обложка'),
        ),
    ]
