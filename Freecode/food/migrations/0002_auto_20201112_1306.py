# Generated by Django 3.0.6 on 2020-11-12 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='picture',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='store/images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='store/images/'),
        ),
    ]
