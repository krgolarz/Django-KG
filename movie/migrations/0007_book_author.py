# Generated by Django 4.2.5 on 2023-10-01 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_rename_release_date_book_publish_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=255, null=True),
        ),
    ]