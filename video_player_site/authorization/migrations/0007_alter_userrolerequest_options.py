# Generated by Django 5.2.4 on 2025-07-23 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0006_alter_userrolerequest_is_approved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userrolerequest',
            options={'verbose_name': 'Role Request', 'verbose_name_plural': 'Role Requests'},
        ),
    ]
