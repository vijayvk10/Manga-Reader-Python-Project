# Generated by Django 5.0.6 on 2024-06-08 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0011_pdffile_chapter_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mangas',
            name='pdf_files',
            field=models.ManyToManyField(blank=True, related_name='mangas', to='manga.pdffile'),
        ),
    ]
