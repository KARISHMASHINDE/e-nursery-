# Generated by Django 3.1.4 on 2021-01-02 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Nursery', '0009_auto_20210102_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]