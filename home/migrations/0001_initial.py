# Generated by Django 4.1.1 on 2022-11-11 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.IntegerField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=50)),
                ('state_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=10)),
                ('contac_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('loc_id', models.IntegerField(primary_key=True, serialize=False)),
                ('loc_name', models.CharField(max_length=50)),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.city')),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('house_id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('address', models.TextField()),
                ('area', models.FloatField()),
                ('bhk', models.IntegerField()),
                ('description', models.TextField()),
                ('sold', models.BooleanField()),
                ('img1', models.ImageField(upload_to='pics')),
                ('img2', models.ImageField(upload_to='pics')),
                ('img3', models.ImageField(upload_to='pics')),
                ('cctv', models.BooleanField()),
                ('children_play_area', models.BooleanField()),
                ('landscape', models.BooleanField()),
                ('garage', models.BooleanField()),
                ('power_backup', models.BooleanField()),
                ('lifts', models.BooleanField()),
                ('cycling_jogging', models.BooleanField()),
                ('fire_fighting', models.BooleanField()),
                ('temple', models.BooleanField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.city')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.location')),
            ],
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('dealer_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('dealer_name', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=10)),
                ('email_id', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('house_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.house')),
            ],
        ),
    ]