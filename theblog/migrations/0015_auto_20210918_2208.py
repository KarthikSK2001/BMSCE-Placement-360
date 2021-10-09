# Generated by Django 3.2.7 on 2021-09-18 16:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0014_post_compensation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='snippet',
            new_name='additional',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title_tag',
            new_name='hiring_type',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='year',
        ),
        migrations.AddField(
            model_name='post',
            name='numberhired',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]