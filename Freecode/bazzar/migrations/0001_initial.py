# Generated by Django 3.0.6 on 2020-11-13 07:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=122)),
                ('address', models.CharField(max_length=122)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazzar.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ShopItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=122)),
                ('price', models.IntegerField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('picture', models.ImageField(blank=True, max_length=255, null=True, upload_to='store/images/')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazzar.DepartmentStore')),
            ],
        ),
    ]
