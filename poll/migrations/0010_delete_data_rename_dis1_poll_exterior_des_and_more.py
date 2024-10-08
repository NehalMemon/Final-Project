# Generated by Django 5.1.1 on 2024-10-04 14:19

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0009_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Data',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='dis1',
            new_name='Exterior_des',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='img1',
            new_name='Exterior_img1',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='img2',
            new_name='Exterior_img2',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='dis2',
            new_name='Homepage_des',
        ),
        migrations.AddField(
            model_name='poll',
            name='Homepage_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='poll',
            name='Interior_des',
            field=tinymce.models.HTMLField(default='default description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poll',
            name='Overall_des',
            field=tinymce.models.HTMLField(default='default description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poll',
            name='interior_img1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='poll',
            name='interior_img2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]