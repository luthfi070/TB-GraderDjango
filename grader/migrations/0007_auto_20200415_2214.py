# Generated by Django 3.0.5 on 2020-04-15 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grader', '0006_auto_20200415_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_pengguna',
            name='username',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
