# Generated by Django 3.1.7 on 2021-05-06 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20210506_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]