# Generated by Django 2.1.7 on 2019-03-01 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dishName', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('allergens', models.CharField(max_length=500)),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastUpdated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numOfSeats', models.IntegerField(default=0)),
                ('date', models.DateTimeField()),
                ('customerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.CustomerAccount')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licenseID', models.CharField(max_length=10)),
                ('rName', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=6)),
                ('phoneNo', models.CharField(max_length=11)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.RestaurantAccount')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=999)),
                ('review_date', models.DateTimeField()),
                ('emoji', models.CharField(max_length=1)),
                ('restaunrantID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='restaunrantID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Restaurant'),
        ),
        migrations.AddField(
            model_name='menu',
            name='restaunrantID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Restaurant'),
        ),
        migrations.AddField(
            model_name='dishes',
            name='menuID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Menu'),
        ),
    ]