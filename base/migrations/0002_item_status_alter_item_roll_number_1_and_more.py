# Generated by Django 4.0.4 on 2022-04-23 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='Roll_Number_1',
            field=models.CharField(editable=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='Roll_Number_2',
            field=models.CharField(editable=False, max_length=10),
        ),
    ]
