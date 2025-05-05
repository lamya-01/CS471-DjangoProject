from django.db import models 


class Book(models.Model): 
  title = models.CharField(max_length = 50) 
  author = models.CharField(max_length = 50) 
  price = models.FloatField(default = 0.0) 
  edition = models.SmallIntegerField(default = 1) 


#lab8 task6
class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
#lab 11
class Student0(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#lab 9
class Card(models.Model):
    card_number = models.IntegerField()


class Department(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField()

class Student1(models.Model):
    name = models.CharField(max_length=100)
    card = models.OneToOneField(Card, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)#many to one
    course = models.ManyToManyField(Course)


#lab 11 task2

class Address2(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city
    
class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ManyToManyField(Address2)

    def __str__(self):
        return self.name


class Book1(models.Model): 
  title = models.CharField(max_length = 50) 
  author = models.CharField(max_length = 50) 
  price = models.FloatField(default = 0.0) 
  edition = models.SmallIntegerField(default = 1) 
  # upload media files into a folder in media folder called ‘documents’
  coverPage = models.FileField(upload_to='documents/')

