# Generated by Django 5.0.6 on 2024-07-05 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_studentmodel_is_anonymous_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
