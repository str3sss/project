# Generated by Django 4.0 on 2022-05-26 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='UserActicleRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('in_bookmark', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.customuser')),
            ],
        ),
    ]
