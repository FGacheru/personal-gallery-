from django.db import models
import datetime as dt

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length =30)
    image = models.ImageField(upload_to = 'images/', default="")
    posted_date= models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length =200)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    class Meta:
        '''
        class method to display images by date posted
        '''
        ordering = ['posted_date']

    def __str__(self):
        return self.description

    @classmethod
    def search_by_category(cls, search_term):
        '''
        Method to filter images by category
        '''
        result = cls.objects.filter(category__category__icontains=search_term)
        return result 

    def search_by_location(cls, search_term):
        '''
        Method to filter images by location
        '''
        result = cls.objects.filter(location__location__icontains=search_term)
        return result

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    @classmethod
    def get_all_categories(cls):
        '''
        Method to get all categories
        '''
        categories = cls.objects.all()
        return categories
    
    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()
        
    @classmethod
    def update_category(cls, id, value):
        cls.objects.filter(id=id).update(name = value)
        
    def __str__(self):
        return self.name 
    
class Location(models.Model):
    name = models.CharField(max_length=30)
    
    @classmethod
    def get_all_locations(cls):
        '''
        Method to get all locations
        '''
        locations = cls.objects.all()
        return locations
    
    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()
        
    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(name = value)
        
    def __str__(self):
        return self.name 
    