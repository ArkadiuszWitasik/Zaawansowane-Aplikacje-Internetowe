# Generated by Django 5.2 on 2025-04-07 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bumbox', '0006_alter_artist_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='./'),
        ),
    ]
