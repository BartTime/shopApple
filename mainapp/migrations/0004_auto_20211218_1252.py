# Generated by Django 3.2.9 on 2021-12-18 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_ip_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
        migrations.DeleteModel(
            name='Ip',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
