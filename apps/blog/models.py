from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.db.models import ForeignKey
from mptt.models import TreeForeignKey, MPTTModel



class Post(models.Model):
    STATUS_OPTIONS = (
        ('published', 'Published'),
        ('draft', 'Draft')
    )

    title = models.CharField(verbose_name='Post Title', max_length=255)
    slug = models.SlugField(verbose_name='URL', max_length=255, blank=True, unique=True)
    description = models.TextField(verbose_name='Brief Description', max_length=500)
    text = models.TextField(verbose_name='Full Post Text')
    category = TreeForeignKey(
        'Category',
        on_delete=models.PROTECT,
        related_name='posts',
        verbose_name='Category'
    )
    thumbnail = models.ImageField(default='default.jpg',
        verbose_name='Post Image',
        blank=True,
        upload_to='images/thumbnails/',
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))]
    )
    status = models.CharField(choices=STATUS_OPTIONS, default='published', verbose_name='Post Status', max_length=10)
    create = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')
    update = models.DateTimeField(auto_now=True, verbose_name='Update Time')
    author = models.ForeignKey(to=User, verbose_name='Author', on_delete=models.SET_DEFAULT, related_name='author_posts',
                               default=1)
    updater = models.ForeignKey(to=User, verbose_name='Updated By', on_delete=models.SET_NULL, null=True,
                                related_name='updater_posts', blank=True)
    fixed = models.BooleanField(verbose_name='Pinned', default=False)

    class Meta:
        db_table = 'blog_post'
        ordering = ['-fixed', '-create']
        indexes = [models.Index(fields=['-fixed', '-create', 'status'])]
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title




class Category(MPTTModel):
    title = models.CharField(max_length=255, verbose_name='Category Title')
    slug = models.SlugField(max_length=255, verbose_name='Category URL', blank=True)
    description = models.TextField(verbose_name='Category Description', max_length=300)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_index=True,
        related_name='children',
        verbose_name='Parent Category'
    )

    class MPTTMeta:

        order_insertion_by = ('title',)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'app_categories'

    def __str__(self):
        return self.title