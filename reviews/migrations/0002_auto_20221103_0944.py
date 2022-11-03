# Generated by Django 3.2.13 on 2022-11-03 09:44

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image_sm',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/'),
        ),
    ]
