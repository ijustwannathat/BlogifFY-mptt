# Generated by Django 5.1 on 2024-09-01 07:16

import django.core.validators
import django.db.models.deletion
import mptt.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Category Title')),
                ('slug', models.SlugField(blank=True, max_length=255, verbose_name='Category URL')),
                ('description', models.TextField(max_length=300, verbose_name='Category Description')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.category', verbose_name='Parent Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'app_categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Post Title')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URL')),
                ('description', models.TextField(max_length=500, verbose_name='Brief Description')),
                ('text', models.TextField(verbose_name='Full Post Text')),
                ('thumbnail', models.ImageField(blank=True, default='default.jpg', upload_to='images/thumbnails/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))], verbose_name='Post Image')),
                ('status', models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='published', max_length=10, verbose_name='Post Status')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Update Time')),
                ('fixed', models.BooleanField(default=False, verbose_name='Pinned')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='author_posts', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('category', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='blog.category', verbose_name='Category')),
                ('updater', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updater_posts', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'db_table': 'blog_post',
                'ordering': ['-fixed', '-create'],
                'indexes': [models.Index(fields=['-fixed', '-create', 'status'], name='blog_post_fixed_0994c8_idx')],
            },
        ),
    ]
