# Generated by Django 3.1.7 on 2021-04-19 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_eligiblestudent_examcenter'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyExamCenter',
            fields=[
            ],
            options={
                'ordering': ['id'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('staff.examcenter',),
        ),
    ]
