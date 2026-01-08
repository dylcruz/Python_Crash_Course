from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=20)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class BlogEntry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text
