# Generated by Django 4.2.7 on 2023-12-13 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppRefugio', '0003_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares/'),
        ),
    ]
