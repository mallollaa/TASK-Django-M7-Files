# Generated by Django 4.1.5 on 2023-02-02 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='avatar',
            field=models.ImageField(default='', upload_to='madia/'),
        ),
    ]
