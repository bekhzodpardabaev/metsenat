# Generated by Django 4.1 on 2022-08-10 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0013_sponsorstothestudent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='choice',
            field=models.TextField(choices=[('Natural person', 'Natural Person'), ('Legal entity', 'Legal Entity')]),
        ),
    ]
