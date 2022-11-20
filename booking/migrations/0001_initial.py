# Generated by Django 3.2.16 on 2022-11-19 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Treatments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technician_no', models.CharField(max_length=5)),
                ('technician_type', models.CharField(max_length=50)),
                ('is_available', models.BooleanField(default=True)),
                ('price', models.FloatField(default=1000.0)),
                ('no_of_days_advance', models.IntegerField()),
                ('start_date', models.DateField()),
                ('technician_image', models.ImageField(default='0.jpeg', upload_to='media')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.technician')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_day', models.DateField()),
                ('end_day', models.DateField()),
                ('amount', models.FloatField()),
                ('booked_on', models.DateTimeField(auto_now=True)),
                ('technician_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.technicians')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.customer')),
            ],
        ),
    ]
