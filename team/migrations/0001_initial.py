# Generated by Django 4.2 on 2024-03-12 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Former_members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('introduction_text', models.TextField()),
                ('member_image', models.ImageField(blank=True, upload_to='')),
                ('linkedin', models.URLField(blank=True, max_length=600)),
                ('orcid', models.URLField(blank=True, max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('introduction_text', models.TextField()),
                ('member_image', models.ImageField(blank=True, upload_to='')),
                ('linkedin', models.URLField(blank=True, max_length=600)),
                ('orcid', models.URLField(blank=True, max_length=600)),
            ],
        ),
    ]