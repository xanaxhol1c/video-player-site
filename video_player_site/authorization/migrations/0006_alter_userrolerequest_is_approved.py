# Generated by Django 5.2.4 on 2025-07-23 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0005_userrolerequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrolerequest',
            name='is_approved',
            field=models.BooleanField(default=None, null=True),
        ),
    ]
