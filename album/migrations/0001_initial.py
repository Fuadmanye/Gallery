# Generated by Django 4.0.4 on 2022-05-30 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='ImageLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='ImagePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_image', models.ImageField(default='album/default.jpg', upload_to='album/')),
                ('image_name', models.CharField(max_length=60)),
                ('image_description', models.TextField()),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('image_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album.imagecategory')),
                ('image_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album.imagelocation')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]