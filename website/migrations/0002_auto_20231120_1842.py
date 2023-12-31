# Generated by Django 3.2.12 on 2023-11-20 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='full_url',
            field=models.URLField(editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='short_url',
            field=models.CharField(editable=False, max_length=10, null=True, unique=True),
        ),
    ]
