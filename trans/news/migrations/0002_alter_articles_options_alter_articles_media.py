# Generated by Django 4.0.3 on 2022-05-03 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Конспект', 'verbose_name_plural': 'Конспекты'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='media', verbose_name='Аудиозапись'),
        ),
    ]
