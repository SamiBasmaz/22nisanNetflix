# Generated by Django 4.2.14 on 2024-07-29 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.FileField(upload_to='actors/', verbose_name='Oyuncu Fotoğrafı')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='aciklama',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, related_name='movies', to='movies.actor'),
        ),
    ]
