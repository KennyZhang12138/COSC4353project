# Generated by Django 3.2.7 on 2022-07-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sd_app', '0011_alter_userprofile_zip_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='address',
            new_name='address_line_1',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
