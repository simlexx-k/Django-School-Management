# Generated by Django 2.2.13 on 2020-12-18 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0009_auto_20201209_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='batches',
            field=models.ManyToManyField(blank=True, null=True, related_name='department_batches', to='academics.Batch'),
        ),
    ]
