# Generated by Django 2.2.1 on 2019-07-12 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ablass_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='antrag',
            old_name='km',
            new_name='kilometers',
        ),
    ]
