# Generated by Django 4.2.11 on 2024-05-03 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=14, unique=True)),
                ('desc', models.CharField(max_length=200)),
                ('points', models.IntegerField(blank=True, default=10, null=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('level', models.CharField(choices=[('L1', 'Level-1'), ('L2', 'Level-2'), ('L3', 'Level-3')], default='L1', max_length=3)),
                ('quiz_link', models.URLField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserGames',
            fields=[
                ('id', models.CharField(default='TINKERCADE', max_length=100, primary_key=True, serialize=False)),
                ('winning_points', models.IntegerField(blank=True, default=0, null=True)),
                ('games', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.games')),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
