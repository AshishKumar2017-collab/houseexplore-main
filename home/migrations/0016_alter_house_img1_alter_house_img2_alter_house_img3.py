# Generated by Django 5.0.6 on 2024-07-04 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_rename_firt_name_customercontacted_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='img1',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='house',
            name='img2',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='house',
            name='img3',
            field=models.ImageField(upload_to='media/'),
        ),
    ]