# Generated by Django 2.2.4 on 2020-10-21 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ExamRetakeApp', '0004_quote_quoter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='name',
        ),
    ]
