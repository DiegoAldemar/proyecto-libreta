# Generated by Django 3.1.2 on 2021-01-04 23:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contactos', '0007_auto_20210104_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactos',
            name='name_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
