from django.db import models


class Category(models.Model):
    '''
    Stores a single category
    '''
    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    '''
    Stores a single product
    '''
    title = models.CharField(max_length=30, null=False)
    price = models.IntegerField()
    published = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT) # CASCADE

    def __str__(self):
        return self.title