# Generated by Django 3.0.7 on 2020-06-11 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20200611_1531'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='comment',
            table='comments',
        ),
        migrations.AlterModelTable(
            name='new',
            table='news',
        ),
        migrations.AlterModelTable(
            name='upvote',
            table='upvotes',
        ),
    ]
