# Generated by Django 3.0.8 on 2022-05-14 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20201107_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
