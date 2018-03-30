from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .search import StudentIndex,UniversityIndex,CourseIndex
import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + (
    'es_index_name', 'es_type_name', 'es_mapping'
)

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length =255)
    def indexing(self):
        obj = UniversityIndex(meta={'id': self.id},name = self.name)
        obj.save()
        return obj.to_dict(include_meta=True)

class Course(models.Model):
    name = models.CharField(max_length = 255, unique = True)
    def indexing(self):
        obj = CourseIndex(meta={'id': self.id},name = self.name)
        obj.save()
        return obj.to_dict(include_meta=True)   

class Student(models.Model):
    YEAR_IN_SCHOOL_CHOICES =(
        ('FR','Freshman'),
        ('SO','Sophomore'),
        ('JR','Junior'),
        ('SR','Senior'),
    )
    year_in_school = models.CharField(max_length =2, choices = YEAR_IN_SCHOOL_CHOICES)
    age = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    first_name = models.CharField(max_length =50)
    last_name = models.CharField(max_length = 50)
    university = models.ForeignKey(University, null= True, blank = True,on_delete = models.SET_NULL)
    courses = models.ManyToManyField(Course, null = True, blank = True )
    # Add indexing method to BlogPost
    def indexing(self):
        obj = StudentIndex(
            meta={'id': self.id},
            year_in_school=self.year_in_school,
            age= self.age,
            first_name=self.first_name,
            last_name=self.last_name,
            university=self.university.name,
            courses= ','.join([course.name for course in self.courses.all()])
        )
        obj.save()
        return obj.to_dict(include_meta=True)