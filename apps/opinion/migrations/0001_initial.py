# Generated by Django 4.1 on 2023-11-11 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=uuid.uuid4, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('watched', models.BooleanField(default=False)),
                ('rewatch', models.BooleanField(default=False)),
                ('anticipation_rating', models.IntegerField(choices=[(10, 'Nope'), (20, 'Okay'), (30, 'Hyped')], default=20)),
                ('rating', models.IntegerField(choices=[(0, 'Not Rated'), (10, 'Nope'), (20, 'Okay'), (30, 'Loved')], default=0)),
                ('favorite', models.BooleanField(default=False)),
                ('comment', models.TextField(blank=True, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opinions', to='movie.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opinions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]