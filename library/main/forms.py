from django import forms
from main.models import Author, Book


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'surname')
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
        }


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'year', 'genre', 'rating')
        labels = {
            'title': 'Название',
            'author': 'Автор',
            'year': 'Год публикации',
            'genre': 'Жанр',
            'rating': 'Рейтинг',
        }
