# Generated by Django 3.1.5 on 2021-03-30 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FieldOfStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_of_study', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='YearOfStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_study', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/face_datas')),
                ('name', models.CharField(max_length=150)),
                ('id_n', models.CharField(max_length=12)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='facex.department')),
                ('field_of_study', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='facex.fieldofstudy')),
                ('year_of_study', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='facex.yearofstudy')),
            ],
        ),
    ]
