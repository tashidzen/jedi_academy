# Generated by Django 3.0.3 on 2020-02-27 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjedaysAcademy', '0006_auto_20200227_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='qu',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
