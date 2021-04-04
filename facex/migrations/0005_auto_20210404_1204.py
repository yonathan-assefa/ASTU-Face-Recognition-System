# Generated by Django 3.1.5 on 2021-04-04 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facex', '0004_student_year_of_study'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id_n',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(unique=True, upload_to='images/face_datas'),
        ),
    ]