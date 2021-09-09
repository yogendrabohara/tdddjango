# Generated by Django 3.1.7 on 2021-09-09 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_text', models.CharField(max_length=50, unique=True, verbose_name='Entry Text')),
            ],
            options={
                'db_table': 'entry',
            },
        ),
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Publication Date')),
                ('byline', models.CharField(max_length=255, verbose_name='Byline')),
                ('publisher', models.CharField(max_length=12, verbose_name='Publisher')),
            ],
        ),
        migrations.CreateModel(
            name='Clue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clue_text', models.CharField(db_index=True, max_length=512, verbose_name='Clue Text')),
                ('theme', models.BooleanField(default=False, verbose_name='Theme')),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xword_data.entry')),
                ('puzzle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xword_data.puzzle')),
            ],
            options={
                'db_table': 'clue',
            },
        ),
    ]
