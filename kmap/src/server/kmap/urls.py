# urls.py
from django.conf.urls import *
from kmap.api import ConceptResource

concept_resource = ConceptResource()

urlpatterns = patterns('',
    (r'^api/', include(concept_resource.urls)),
)