# Generated by Django 4.2 on 2024-01-10 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0004_publication_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='next_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next', to='publications.publication'),
        ),
        migrations.AddField(
            model_name='publication',
            name='previous_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous', to='publications.publication'),
        ),
    ]
