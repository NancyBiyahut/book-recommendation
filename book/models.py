from django.db import models

class Bookmain(models.Model):
    ISBN = models.CharField(max_length=250)
    bookTitle = models.CharField(max_length=500)
    bookAuthor = models.CharField(max_length=500)
    yearOfPublication = models.IntegerField()
    publisher = models.CharField(max_length=500)
    imageUrlS = models.URLField()
    imageUrlM = models.URLField()
    imageUrlL = models.URLField()
    
    def __str__(self):
            return self.bookTitle
