# Generated by Django 3.1.7 on 2021-09-09 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xword_data', '0002_auto_20210909_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puzzle',
            name='date',
            field=models.DateField(verbose_name='Publication Date'),
        ),
        migrations.AlterField(
            model_name='puzzle',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Title'),
        ),
    ]
