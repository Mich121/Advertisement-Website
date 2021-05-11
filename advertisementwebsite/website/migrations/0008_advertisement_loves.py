# Generated by Django 3.1.7 on 2021-05-11 12:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0007_auto_20210509_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='loves',
            field=models.ManyToManyField(related_name='favorite_advert', to=settings.AUTH_USER_MODEL),
        ),
    ]
