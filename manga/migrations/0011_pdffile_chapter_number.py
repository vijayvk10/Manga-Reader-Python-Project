# Generated by Django 5.0.6 on 2024-06-08 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0010_remove_library_manga_image_remove_library_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdffile',
            name='chapter_number',
            field=models.IntegerField(default=1),
        ),
    ]
