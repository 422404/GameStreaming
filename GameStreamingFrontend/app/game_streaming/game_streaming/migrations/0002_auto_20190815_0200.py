# Generated by Django 2.2.4 on 2019-08-15 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_streaming', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='available',
            new_name='is_available',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='hidden',
            new_name='is_hidden',
        ),
    ]