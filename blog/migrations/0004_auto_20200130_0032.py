# Generated by Django 2.2.5 on 2020-01-29 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200130_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.ImageField(upload_to='imageblog/'),
        ),
    ]
