# Generated by Django 4.0.5 on 2022-06-02 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='women',
            old_name='titel',
            new_name='title',
        ),
    ]