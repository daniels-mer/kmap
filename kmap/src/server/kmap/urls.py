# urls.py
from django.conf.urls import *
from kmap.api import ConceptResource
from tastypie.api import Api

concept_resource = ConceptResource()

v1_api = Api(api_name='v1')
v1_api.register(ConceptResource())

urlpatterns = patterns('',
#     (r'^api/', include(concept_resource.urls)),
    (r'^api/', include(v1_api.urls)),
)