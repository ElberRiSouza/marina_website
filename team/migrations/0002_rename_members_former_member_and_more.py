# Generated by Django 4.2 on 2024-03-12 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Members',
            new_name='Former_member',
        ),
        migrations.RenameModel(
            old_name='Former_members',
            new_name='Member',
        ),
    ]
