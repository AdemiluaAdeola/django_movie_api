from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=2000)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Movie(models.Model):
    category = models.ManyToManyField(Category)
    image = models.URLField()
    title = models.CharField(max_length=20000)
    movie_url = models.URLField()
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Series(models.Model):
    category = models.ManyToManyField(Category)
    image = models.URLField()
    title = models.CharField(max_length=20000)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Series"
        verbose_name_plural = "Series"

    def __str__(self):
        return self.title

class Season(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    image = models.URLField()
    title = models.CharField(max_length=20000)
    description = models.TextField()

    def __str__(self):
        return self.series.title + " - " + self.title

class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    title = models.CharField(max_length=20000)
    movie_url = models.URLField()

    def __str__(self):
        return self.season.series.title + " - " + self.season.title + " - " + self.title
