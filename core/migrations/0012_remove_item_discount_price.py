# Generated by Django 2.2.14 on 2022-12-20 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_item_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='discount_price',
        ),
    ]
