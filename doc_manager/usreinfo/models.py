from django.db import models

# Create your models here.

class Userdata(models.Model):
    OPTIONS = [('LS','liscense'), 
    ('ID','Identity'), 
    ('ED','education'), 
    ('CR,','certificate'), 
    ('OT','others')]
    user_name = models.CharField(max_length=200)
    doc_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=OPTIONS,default=OPTIONS[-1])
    link = models.URLField(max_length = 200)

    def __str__(self):
        return self.doc_name