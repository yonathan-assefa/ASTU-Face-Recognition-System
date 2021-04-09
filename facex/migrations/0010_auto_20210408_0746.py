# Generated by Django 3.1.5 on 2021-04-08 07:46

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('facex', '0009_auto_20210407_0756'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=120)),
                ('field_of_study', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='school_program', chained_model_field='school_program', on_delete=django.db.models.deletion.CASCADE, to='facex.fieldofstudy')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_program', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='dept',
        ),
        migrations.AddField(
            model_name='department',
            name='field_of_study',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='school_program', chained_model_field='school_program', default='', on_delete=django.db.models.deletion.CASCADE, to='facex.fieldofstudy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='department',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='school', chained_model_field='school', default='', on_delete=django.db.models.deletion.CASCADE, to='facex.department'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='field_of_study',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='school_program', chained_model_field='school_program', on_delete=django.db.models.deletion.CASCADE, to='facex.fieldofstudy'),
        ),
        migrations.AlterField(
            model_name='student',
            name='year_of_study',
            field=models.CharField(choices=[('FM', 'Freshman'), ('SO', 'Sopomer'), ('JU', 'Juniour'), ('SE', 'Senior'), ('GC', 'GC')], max_length=2),
        ),
        migrations.DeleteModel(
            name='YearOfStudy',
        ),
        migrations.AddField(
            model_name='school',
            name='school_program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='facex.schoolprogram'),
        ),
        migrations.AddField(
            model_name='department',
            name='school',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='field_of_study', chained_model_field='field_of_study', default='', on_delete=django.db.models.deletion.CASCADE, to='facex.school'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='school_program',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='facex.schoolprogram'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fieldofstudy',
            name='school_program',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='facex.schoolprogram'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='school',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='field_of_study', chained_model_field='field_of_study', default='', on_delete=django.db.models.deletion.CASCADE, to='facex.school'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='school_program',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='facex.schoolprogram'),
            preserve_default=False,
        ),
    ]