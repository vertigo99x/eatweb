# Generated by Django 3.2.4 on 2022-10-31 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20221030_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditems',
            name='total_raters',
            field=models.CharField(default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='fooditems',
            name='total_rating',
            field=models.CharField(default='0', max_length=255),
        ),
    ]
