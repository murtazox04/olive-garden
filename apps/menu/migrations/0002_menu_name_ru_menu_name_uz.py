# Generated by Django 5.0.6 on 2024-06-01 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='name_uz',
            field=models.CharField(max_length=100, null=True),
        ),
    ]