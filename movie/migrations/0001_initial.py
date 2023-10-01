# Generated by Django 4.2.5 on 2023-10-01 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('publish_date', models.DateField()),
                ('vote_count', models.IntegerField()),
                ('vote_average', models.DecimalField(decimal_places=2, max_digits=5)),
                ('author', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovieStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_count', models.IntegerField()),
                ('vote_average', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=1000)),
                ('cast', models.CharField(max_length=1000)),
                ('homepage', models.URLField()),
                ('director', models.CharField(max_length=1000)),
                ('keywords', models.CharField(max_length=1000)),
                ('overview', models.TextField()),
                ('runtime_minutes', models.IntegerField()),
                ('genres', models.CharField(max_length=1000)),
                ('production_companies', models.CharField(max_length=1000)),
                ('release_date', models.DateField()),
                ('statistics', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='movie.moviestatistics')),
            ],
        ),
    ]
