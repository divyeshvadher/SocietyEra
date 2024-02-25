# Generated by Django 4.2.3 on 2024-02-16 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_alter_reference_id_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('president', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
            ],
        ),
    ]
