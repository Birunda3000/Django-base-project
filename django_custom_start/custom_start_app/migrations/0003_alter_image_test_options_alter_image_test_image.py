# Generated by Django 4.0.4 on 2022-05-27 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_start_app', '0002_image_test'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image_test',
            options={'verbose_name_plural': 'image_tests'},
        ),
        migrations.AlterField(
            model_name='image_test',
            name='image',
            field=models.ImageField(blank=True, upload_to='images_test_folder/'),
        ),
    ]