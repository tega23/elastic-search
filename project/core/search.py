from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date,Integer
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.create_connection()


class StudentIndex(DocType):
    class Meta:
        index = 'student-index'
    year_in_school = Text()
    age = Iteger()
    first_name = Text()
    last_name = Text()
    university = Text()
    courses = Text()

def bulk_indexing():
    StudentIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.Student.objects.all().iterator()))
