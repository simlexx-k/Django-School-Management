# Generated by Django 2.2.13 on 2020-10-09 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20201009_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissionstudent',
            name='counsel_comment',
            field=models.ManyToManyField(to='teachers.Teacher'),
        ),
    ]