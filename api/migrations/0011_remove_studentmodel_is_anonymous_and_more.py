# Generated by Django 5.0.6 on 2024-07-05 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentmodel',
            name='is_anonymous',
        ),
        migrations.RemoveField(
            model_name='studentmodel',
            name='is_authenticated',
        ),
        migrations.AlterField(
            model_name='loginmodel',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
