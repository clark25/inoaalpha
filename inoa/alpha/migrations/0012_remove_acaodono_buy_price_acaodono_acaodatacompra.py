# Generated by Django 4.0.6 on 2022-07-25 05:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0011_alter_acaohistorico_date_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acaodono',
            name='buy_price',
        ),
        migrations.AddField(
            model_name='acaodono',
            name='acaodatacompra',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='alpha.acaohistorico'),
            preserve_default=False,
        ),
    ]
