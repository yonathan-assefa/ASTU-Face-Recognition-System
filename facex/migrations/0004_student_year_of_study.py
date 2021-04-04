# Generated by Django 3.1.5 on 2021-04-03 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facex', '0003_yearofstudy'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='year_of_study',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='facex.yearofstudy'),
            preserve_default=False,
        ),
    ]
