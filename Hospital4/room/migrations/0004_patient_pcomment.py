# Generated by Django 3.1.7 on 2021-03-17 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_remove_patient_pcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='pcomment',
            field=models.CharField(default='No comments', max_length=50),
        ),
    ]
