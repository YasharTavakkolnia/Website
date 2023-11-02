from django.db import models

class Work(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey('Category',related_name='work',verbose_name=('دسته بندی'), on_delete=models.CASCADE)
    image = models.ImageField(upload_to='works',blank= True , null= True)
    client = models.CharField(max_length=150)
    desc = models.TextField()
    date = models.CharField(max_length=150)
    image1 = models.ImageField(upload_to='works',blank= True , null= True)
    image2 = models.ImageField(upload_to='works',blank= True , null= True)
    image3 = models.ImageField(upload_to='works',blank= True , null= True)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    def __str__(self):
        return self.title



