# Generated by Django 4.1 on 2023-10-27 19:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bubble',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=uuid.uuid4, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=32, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(32)], verbose_name='name')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bubbles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'bubbles',
            },
        ),
        migrations.CreateModel(
            name='BubbleUser',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=uuid.uuid4, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('bubble', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bubble_users', to='bubble.bubble')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bubble_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'bubble_users',
            },
        ),
    ]