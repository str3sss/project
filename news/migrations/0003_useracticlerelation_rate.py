# Generated by Django 4.0 on 2022-05-26 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_article_useracticlerelation'),
    ]

    operations = [
        migrations.AddField(
            model_name='useracticlerelation',
            name='rate',
            field=models.SmallIntegerField(choices=[(-1, -1), (0, 0), (1, 1)], default=0),
        ),
    ]
