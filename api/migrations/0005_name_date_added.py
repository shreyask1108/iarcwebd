# Generated by Django 4.1.3 on 2023-06-10 17:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_name_delete_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]