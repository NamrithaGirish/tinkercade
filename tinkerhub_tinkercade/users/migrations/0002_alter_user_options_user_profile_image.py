# Generated by Django 4.2.11 on 2024-05-03 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-email']},
        ),
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.URLField(blank=True, max_length=3000, null=True),
        ),
    ]
