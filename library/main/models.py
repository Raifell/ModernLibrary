from django.db import models
from pytils.translit import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    name = models.CharField('Genre', max_length=255)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField('Name', max_length=255)
    surname = models.CharField('Surname', max_length=255)
    slug = models.CharField('Slug', max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.surname)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify('{}-{}'.format(self.name, self.surname))
        super(Author, self).save(force_insert, force_update, using, update_fields)


class Book(models.Model):
    title = models.CharField('Title', max_length=255)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, verbose_name='Author')
    year = models.PositiveIntegerField('Published year', validators=[MinValueValidator(500), MaxValueValidator(2023)])
    genre = models.ManyToManyField('Genre')
    rating = models.PositiveIntegerField('Rating', validators=[MinValueValidator(1), MaxValueValidator(10)])
    slug = models.CharField('Slug', max_length=255, unique=True, blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify('{}-{}'.format(self.title, self.author.surname))
        super(Book, self).save(force_insert, force_update, using, update_fields)
