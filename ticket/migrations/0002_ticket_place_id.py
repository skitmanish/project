# Generated by Django 2.1.5 on 2019-09-28 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='place_id',
            field=models.IntegerField(default=302),
        ),
    ]
