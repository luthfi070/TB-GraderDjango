# Generated by Django 3.0.5 on 2020-04-16 05:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('grader', '0008_auto_20200415_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_pengguna',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
    ]
