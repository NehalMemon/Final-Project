# Generated by Django 5.1.1 on 2024-09-20 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_alter_poll_id_alter_poll_img1_alter_poll_img2'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]