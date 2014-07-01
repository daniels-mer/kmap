# -*- coding: utf-8 -*-

"""
    :mod:`urls` -- 
    ===================================
    
    .. module:: src.server.kmap
          :synopsis: Defines the url dispatchers .
    .. moduleauthor:: Daniel Santonja
        
    :License: GPL (https://gnu.org/licenses/gpl.html)
    
    :Date last change:
    
    :Version:
"""

from django.conf.urls import patterns, url, include
from kmap.api import ConceptResource, LinkResource
from tastypie.api import Api
from kmap import views

concept_resource = ConceptResource()

v1_api = Api(api_name='v1')
v1_api.register(ConceptResource())
v1_api.register(LinkResource())

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
    url(r'^index.html$', views.index, name='index'),
    url(r'^navigate.html$', views.navigate, name='navigate'),
    url(r'^learn.html$', views.navigate, name='learn'),
)