# Generated by Django 4.2.14 on 2024-07-30 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='kategori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.kategori'),
        ),
    ]