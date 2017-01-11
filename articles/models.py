from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=150, verbose_name="Tytul")
	content = models.TextField(verbose_name="Zawartosc")
	created = models.DateTimeField(verbose_name="Data publikacji")
	image = models.TextField(max_length=100000, verbose_name="Obrazek")

	def __unicode__(self): #definicja do panelu Administracyjnego
		return self.title


class Comment(models.Model):
	name = models.CharField(max_length=150, verbose_name="Uzytkownik")
	content = models.TextField(verbose_name="Komentarz")
	published = models.DateTimeField(verbose_name="Data publikacji")
	article = models.ForeignKey(Article)


	def __unicode__(self):
		return self.name