from django.db import models
from django.contrib.auth.models import User



class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.authorUser.username}"

class Category(models.Model):
    NameCategory = models.CharField(max_length=64, unique = True)
    
class AD(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tank = 'ta'
    hiller = 'hi'
    dd = 'dd'
    vendor = 've'
    guildmaster = 'gm'
    quiest = 'qu'
    smith = 'sm'
    hunter = 'hu'
    alchemist = 'al'
    mistique = 'mi'
    
    how_choise = (
        (tank, 'Танк'),
        (hiller, 'Хил'),
        (dd, 'ДД'), 
        (vendor, 'Торговец'), 
        (guildmaster, 'Гилдмастер'),
        (quiest, 'Квестгивер'),
        (smith, 'Кузнец'),
        (hunter, 'Кожевник'),
        (alchemist, 'Зельевар'),
        (mistique, 'Мастер заклинаний'),
        
    )
    categoryType = models.CharField(max_length = 2, choices = how_choise, default = dd)
    dataCategory = models.DateTimeField(auto_now_add = True)
    category = models.ManyToManyField(Category, through = "ADCategory")
    title = models.CharField(max_length=128)
    text = models.TextField()

    """ def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
 """
    def preview(self):
        return self.text[0:124] + '...'
    
    def __str__(self):
       return f'Пост #{self.pk} - Название: {self.title}'
    
    def get_absolute_url(self): # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
       return f'/post/{self.id}'
    
class ADCategory(models.Model):
    postThrough = models.ForeignKey(AD, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

#Отклик
class Responce(models.Model):
    responceAD = models.ForeignKey(AD, on_delete=models.CASCADE)
    responceUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.responceAD.author.authorUser.username


# Create your models here.
