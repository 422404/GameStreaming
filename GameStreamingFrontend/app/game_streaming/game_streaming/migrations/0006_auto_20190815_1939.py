# Generated by Django 2.2.4 on 2019-08-15 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_streaming', '0005_remove_game_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='description_short',
            field=models.TextField(blank=True, max_length=120, verbose_name='Short description of the game'),
        ),
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(blank=True, max_length=500, verbose_name='Description of the game'),
        ),
    ]
