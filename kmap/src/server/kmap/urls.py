# urls.py
from django.conf.urls import *
from kmap.api import ConceptResource, LinkResource
from tastypie.api import Api

concept_resource = ConceptResource()

v1_api = Api(api_name='v1')
v1_api.register(ConceptResource())
v1_api.register(LinkResource())

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
#     (r'^api/', include(v1_api.urls)),
)