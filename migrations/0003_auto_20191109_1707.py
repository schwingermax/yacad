# Generated by Django 2.2.7 on 2019-11-09 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yacad', '0002_auto_20191109_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='duration',
        ),
        migrations.AddField(
            model_name='brand',
            name='lifetime',
            field=models.PositiveIntegerField(default=20, help_text='in Years'),
            preserve_default=False,
        ),
    ]
