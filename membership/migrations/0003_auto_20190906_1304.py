# Generated by Django 2.2.4 on 2019-09-06 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_auto_20190814_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='membership_type',
            field=models.CharField(choices=[('Enterprise', 'ent'), ('Professional', 'pro'), ('Free', 'free')], default='Free', max_length=30),
        ),
    ]
