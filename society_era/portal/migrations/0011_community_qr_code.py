# Generated by Django 4.2.3 on 2024-02-25 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_community_uuid_alter_community_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qrcodes/'),
        ),
    ]
