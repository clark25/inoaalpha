# Generated by Django 4.0.6 on 2022-07-22 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0008_acaodono_buy_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acaohistorico',
            options={'ordering': ['-date_price']},
        ),
    ]
