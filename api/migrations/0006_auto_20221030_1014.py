# Generated by Django 3.2.4 on 2022-10-30 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_vendor_total_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=255)),
                ('recipient', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
                ('banner', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['date_created'],
            },
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='food_id_array',
            new_name='client',
        ),
        migrations.AddField(
            model_name='orders',
            name='food_items_array',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='order_description',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor',
            name='total_revenue',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vendor',
            name='wallet_balance',
            field=models.IntegerField(default=0),
        ),
    ]
