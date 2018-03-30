from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date,Integer,Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.create_connection()


class StudentIndex(DocType):
    class Meta:
        index = 'student-index'
    year_in_school = Text()
    age = Integer()
    first_name = Text()
    last_name = Text()
    university = Text()
    courses = Text()

class UniversityIndex(DocType):
    class Meta:
        index = 'university-index'
    name = Text(),


class CourseIndex(DocType):
    class Meta:
        index = 'course-index'
    name = Text()

def bulk_indexing():
    StudentIndex.init()
    UniversityIndex.init()
    CourseIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.Student.objects.all().iterator()))
    bulk(client=es, actions=(b.indexing() for b in models.University.objects.all().iterator()))
    bulk(client=es, actions=(b.indexing() for b in models.Course.objects.all().iterator()))


"""
def search(age):
    s = Search().filter('term', age = age)
    response = s.execute()
    return response

"""
def search(university):
    s = Search().filter('term', university = university)
    response = s.execute()
    return response