# Generated by Django 4.1 on 2022-08-15 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tutorial_app', '0004_videotutorial_video_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='videotutorial',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True),
        ),
    ]
