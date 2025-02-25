# Generated by Django 4.2.8 on 2023-12-25 16:51

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
            name='Iteam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('weight', models.CharField(blank=True, max_length=1000, null=True)),
                ('height', models.CharField(blank=True, max_length=1000, null=True)),
                ('length', models.CharField(blank=True, max_length=1000, null=True)),
                ('data_posted', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(max_length=10, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
