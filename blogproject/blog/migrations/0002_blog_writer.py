# Generated by Django 3.0.8 on 2020-07-20 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='writer',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
