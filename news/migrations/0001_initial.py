# Generated by Django 3.2 on 2022-10-16 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('body', models.TextField()),
                ('feature_image', models.FileField(upload_to='news-gallery/')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'News',
                'ordering': ['pub_date'],
            },
        ),
    ]
