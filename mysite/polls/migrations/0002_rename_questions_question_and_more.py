# Generated by Django 5.0.6 on 2024-06-07 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='questions',
            new_name='question',
        ),
    ]
