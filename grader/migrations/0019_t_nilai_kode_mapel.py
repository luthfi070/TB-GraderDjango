# Generated by Django 3.0.5 on 2020-04-19 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grader', '0018_t_matkul_kode_mapel'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_nilai',
            name='kode_mapel',
            field=models.CharField(default='kode', max_length=15),
        ),
    ]
