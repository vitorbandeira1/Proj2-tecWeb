# Generated by Django 3.2 on 2021-05-11 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviegenerator', '0002_auto_20210511_0832'),
    ]

    operations = [
        migrations.RenameField(
            model_name='production',
            old_name='gender',
            new_name='genres',
        ),
        migrations.RenameField(
            model_name='production',
            old_name='type',
            new_name='type_of',
        ),
    ]
