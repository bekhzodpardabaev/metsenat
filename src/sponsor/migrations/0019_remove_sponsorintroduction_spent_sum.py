# Generated by Django 4.1 on 2022-08-12 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0018_alter_sponsorstothestudent_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsorintroduction',
            name='spent_sum',
        ),
    ]