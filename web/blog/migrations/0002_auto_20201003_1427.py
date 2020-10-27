# Generated by Django 3.1.2 on 2020-10-03 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True, verbose_name='Url'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200, verbose_name='Author')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_comment', to='blog.blog')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_comment', to='blog.comment')),
            ],
        ),
    ]
