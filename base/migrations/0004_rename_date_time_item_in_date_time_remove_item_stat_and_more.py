# Generated by Django 4.0.4 on 2022-04-24 15:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_item_date_remove_item_time_item_date_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='date_time',
            new_name='in_date_time',
        ),
        migrations.RemoveField(
            model_name='item',
            name='stat',
        ),
        migrations.RemoveField(
            model_name='item',
            name='status',
        ),
        migrations.AddField(
            model_name='item',
            name='out_date_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
