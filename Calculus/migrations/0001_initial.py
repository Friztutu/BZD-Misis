# Generated by Django 3.2.18 on 2023-07-02 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResultTask1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diameter', models.FloatField()),
                ('vertical_length', models.FloatField()),
                ('num_accurate', models.FloatField()),
                ('scheme', models.CharField(max_length=32)),
                ('distance_between', models.FloatField()),
                ('section', models.FloatField()),
                ('length', models.FloatField()),
                ('depth', models.FloatField()),
                ('total_resistance', models.FloatField()),
                ('normative_resistance', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Task1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('power', models.PositiveSmallIntegerField(default=None)),
                ('amperage', models.PositiveSmallIntegerField(default=None)),
                ('scheme', models.CharField(max_length=32)),
                ('soil', models.CharField(max_length=64)),
                ('climate_zone', models.PositiveSmallIntegerField()),
            ],
        ),
    ]