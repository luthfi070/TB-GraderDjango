# Generated by Django 3.0.5 on 2020-04-16 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grader', '0011_t_matkul_kelas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_matkul',
            name='nama_mapel',
            field=models.CharField(max_length=50),
        ),
    ]
