# Generated by Django 4.0.4 on 2022-05-07 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_articles_content_alter_articles_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='content',
        ),
        migrations.AddField(
            model_name='articles',
            name='content_file',
            field=models.FileField(blank=True, null=True, upload_to='media', verbose_name='Текстовый документ'),
        ),
        migrations.AddField(
            model_name='articles',
            name='content_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на текстовый документ'),
        ),
    ]
