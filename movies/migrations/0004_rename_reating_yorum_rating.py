# Generated by Django 4.2.14 on 2024-07-29 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_yorum'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yorum',
            old_name='reating',
            new_name='rating',
        ),
    ]
