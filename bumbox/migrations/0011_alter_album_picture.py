# Generated by Django 5.2 on 2025-04-11 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bumbox', '0010_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='picture',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
