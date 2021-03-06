# Generated by Django 2.2.5 on 2020-01-29 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='body',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='pub_date',
            field=models.CharField(max_length=220),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
