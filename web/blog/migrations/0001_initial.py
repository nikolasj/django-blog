# Generated by Django 3.1.2 on 2020-10-03 04:48

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('poster', models.ImageField(default='blog_images/no_image.png', upload_to=blog.models.poster_upload_to, verbose_name='Poster')),
                ('publish', models.DateTimeField(auto_now_add=True, verbose_name='Publish date')),
                ('draft', models.BooleanField(default=True, verbose_name='Draft')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]
