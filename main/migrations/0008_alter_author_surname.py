# Generated by Django 4.0.6 on 2022-07-25 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_news_author_alter_news_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='surname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия'),
        ),
    ]