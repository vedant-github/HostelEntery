# Generated by Django 4.0.4 on 2022-04-26 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_item_in_date_time_alter_item_out_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='in_date_time',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='out_date_time',
            field=models.DateTimeField(editable=False),
        ),
    ]
