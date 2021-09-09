from django.db import models
from django.db.models import indexes

# Create your models here.


class Puzzle(models.Model):
    class Meta(object):
        db_table = 'puzzle'

    title = models.CharField(
        'Title', blank=True, null=True, max_length=255
    )
    date = models.DateField(
        'Publication Date', blank=False, null=False
    )
    byline = models.CharField(
        'Byline', blank=False, null=False, max_length=255
    )
    publisher = models.CharField(
        'Publisher', blank=False, null=False, max_length=12
    )


class Entry(models.Model):
    class Meta(object):
        db_table = 'entry'

    entry_text = models.CharField(
        'Entry Text', blank=False, null=False, unique=True, max_length=50
    )


class Entry(models.Model):
    class Meta(object):
        db_table = 'entry'

    entry_text = models.CharField(
        'Entry Text', blank=False, null=False, unique=True, max_length=50
    )


class Clue(models.Model):
    class Meta(object):
        db_table = 'clue'

    entry = models.ForeignKey(
        Entry, on_delete=models.CASCADE, db_index=True
    )
    puzzle = models.ForeignKey(
        Puzzle, on_delete=models.CASCADE
    )
    clue_text = models.CharField(
        'Clue Text', blank=False, null=False, max_length=512, db_index=True
    )
    theme = models.BooleanField(
        'Theme', default=False
    )
