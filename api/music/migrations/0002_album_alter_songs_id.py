# Generated by Django 4.1.4 on 2023-01-16 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('date_publish', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='songs',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
