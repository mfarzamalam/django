# Generated by Django 3.1.7 on 2021-03-17 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='pemail',
            new_name='p_email',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='pid',
            new_name='p_id',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='pname',
            new_name='p_name',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='ppass',
            new_name='p_pass',
        ),
    ]
