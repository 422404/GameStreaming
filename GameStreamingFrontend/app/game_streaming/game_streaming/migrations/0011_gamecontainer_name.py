# Generated by Django 2.2.4 on 2019-08-17 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_streaming', '0010_auto_20190817_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamecontainer',
            name='name',
            field=models.CharField(default='bf6762802498a0f4659cc395f21407288aac3869836c9b57f5ed1839e8d51986', max_length=64, verbose_name='Container name'),
            preserve_default=False,
        ),
    ]
