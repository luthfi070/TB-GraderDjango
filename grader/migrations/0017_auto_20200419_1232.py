# Generated by Django 3.0.5 on 2020-04-19 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grader', '0016_auto_20200418_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_pengguna',
            name='kelas',
            field=models.CharField(choices=[('SI4301', 'SI4301'), ('SI4302', 'SI4302'), ('SI4303', 'SI4303')], default='SI4301', max_length=15),
        ),
    ]