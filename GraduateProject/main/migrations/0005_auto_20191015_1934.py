# Generated by Django 2.2.6 on 2019-10-15 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20191008_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='computerScore',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
