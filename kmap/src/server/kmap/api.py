# -*- coding: utf-8 -*-

"""
    :mod:`api` -- 
    ===================================
    
    .. module:: src.server.kmap
          :synopsis: .
    .. moduleauthor:: Daniel Santonja
        
    :License: GPL (https://gnu.org/licenses/gpl.html)
    
    :Date last change:
    
    :Version:
"""
import sys
from tastypie.resources import Resource
from tastypie.authorization import Authorization
from tastypie.bundle import Bundle
from tastypie import fields
from kmap.models import Concept, Link
from kmap.serializers import ConceptJSONSerializer
from neo4django.db import models

class ConceptResource(Resource):
    # Just like a Django ``Form`` or ``Model``, we're defining all the
    # fields we're going to handle with the API here.
    
    label = fields.CharField(attribute='label', unique=True)
    description = fields.CharField(attribute='description', null=True)

    links = fields.ToManyField(to='kmap.api.LinkResource', attribute="links", null=True, blank=True)

    class Meta:
        resource_name = 'concept'
        object_class = Concept
        authorization = Authorization()
        serializer = ConceptJSONSerializer()
        
    
    # The following methods will need overriding regardless of your
    # data source.
    def detail_uri_kwargs(self, bundle_or_obj):
        """
            ..method::detail_uri_kwargs(bundle_or_obj)
            
            Given a Bundle or an object, it returns the extra kwargs needed 
            to generate a detail URI.
            
            :param bundle_or_obj: Either a bundle.
            :type bundle_or_obj: Bundle or obj.
            
            :returns: The primary key
            :rtype: Dictionary.
            
        """
        kwargs = {}
        
        if isinstance(bundle_or_obj, Bundle):
            bool(bundle_or_obj.obj)
            kwargs['pk'] = bundle_or_obj.obj.label
        else:
            kwargs['pk'] = bundle_or_obj[0].label
        
#         if isinstance(bundle_or_obj, Bundle):
#             kwargs[self._meta.detail_uri_name] = getattr(bundle_or_obj.obj, self._meta.detail_uri_name)
#         else:
#             kwargs[self._meta.detail_uri_name] = getattr(bundle_or_obj, self._meta.detail_uri_name)
        return kwargs

    def get_object_list(self, request):
        """
            ..method::get_object_list(request)
            
            Gets raw list (can use request to narrow the query?)
            
            :param param1: Parameter description.
            :type param1: Parameter type.
            
            :returns: Return value
            :rtype: Return type.
            
        """
        sys.stderr.write("get_object_list is called\n")
        results = Concept.objects.all()

        return results
    
    def obj_get_list(self, bundle, **kwargs):
        # Calls apply_filters that calls to get_object_list skipped in this 
        # prototype. Then calls for authorization, skipped too.
        sys.stderr.write("obj_get_list is called\n")
        return self.get_object_list(bundle.request)

    def obj_get(self, bundle, **kwargs):
        #Get one obj
        sys.stderr.write("obj_get is called\n")
        label = kwargs['pk']
        sys.stderr.write("obj_get is called label:%s\n"%str(label))
        resource = Concept.objects.filter(label__iexact=label)
        sys.stderr.write("obj_get is called resource:%s\n"%type(resource))
        sys.stderr.write("obj_get is called prueba %s\n"% type(self._meta.object_class()))
        return resource[0] #Without the slice it returned a Queryset instead of a model, breaking the entire program

    def obj_create(self, bundle, **kwargs):
        #creates an object
        sys.stderr.write("obj_create is called \n")
        bundle.obj = Concept()
        bundle = self.full_hydrate(bundle)

        new_concept = Concept.objects.create(label=bundle.obj.label,
                                             description=bundle.obj.desciption)
        
        new_concept.save()
        return bundle

    def obj_update(self, bundle, **kwargs):
        #updates an object, needs more coding
        return self.obj_create(bundle, **kwargs)

    def obj_delete_list(self, bundle, **kwargs):
        results = Concept.objects.all()

        for result in results:
            result.delete()


    def obj_delete(self, bundle, **kwargs):
        result = Concept.objects.filter(label=kwargs['pk'])

        result.delete()

    def rollback(self, bundles):
        pass
    
    def dehydrate(self, bundle):
        links = []
        concept = Concept.objects.get(label=bundle.data["label"])
        for link in concept.links.all():
            links.append({"type":link.type, "label":link.opposite(bundle.data["label"]).label})
        bundle.data["links"] = links
        return bundle
    
class LinkResource(Resource):
    # Just like a Django ``Form`` or ``Model``, we're defining all the
    # fields we're going to handle with the API here.
#     id = fields.IntegerField(attribute='id', unique=True)
    
    link_type = fields.CharField(attribute='type', unique=False)

    concepts = fields.ToManyField(to='kmap.api.ConceptResource', attribute="concepts", null=True, blank=True)

    class Meta:
        resource_name = 'link'
        object_class = Link
        authorization = Authorization()
        
        
    
    # The following methods will need overriding regardless of your
    # data source.
    def detail_uri_kwargs(self, bundle_or_obj):
        """
            ..method::detail_uri_kwargs(bundle_or_obj)
            
            Given a Bundle or an object, it returns the extra kwargs needed 
            to generate a detail URI.
            
            :param bundle_or_obj: Either a bundle.
            :type bundle_or_obj: Bundle or obj.
            
            :returns: The primary key
            :rtype: Dictionary.
            
        """
        kwargs = {}
        
        if isinstance(bundle_or_obj, Bundle):
            bool(bundle_or_obj.obj)
            kwargs['pk'] = bundle_or_obj.obj.type
        else:
            kwargs['pk'] = bundle_or_obj[0].type
        
#         if isinstance(bundle_or_obj, Bundle):
#             kwargs[self._meta.detail_uri_name] = getattr(bundle_or_obj.obj, self._meta.detail_uri_name)
#         else:
#             kwargs[self._meta.detail_uri_name] = getattr(bundle_or_obj, self._meta.detail_uri_name)
        return kwargs

    def get_object_list(self, request):
        """
            ..method::get_object_list(request)
            
            Gets raw list (can use request to narrow the query?)
            
            :param param1: Parameter description.
            :type param1: Parameter type.
            
            :returns: Return value
            :rtype: Return type.
            
        """
        sys.stderr.write("get_object_list is called\n")
        results = Link.objects.all()

        return results
    
    def obj_get_list(self, bundle, **kwargs):
        # Calls apply_filters that calls to get_object_list skipped in this 
        # prototype. Then calls for authorization, skipped too.
        sys.stderr.write("obj_get_list is called\n")
        return self.get_object_list(bundle.request)

    def obj_get(self, bundle, **kwargs):
        #Beacause there are no "unique" link it returns a list
        return self.get_object_list(bundle.request)
        
    def obj_create(self, bundle, **kwargs):
        #creates an object
        sys.stderr.write("obj_create is called \n")
        bundle.obj = Concept()
        bundle = self.full_hydrate(bundle)

        new_link = Concept.objects.create(type=bundle.obj.type)
        concept = Concept.obects.get(bundle.obj.concepts[0])
        new_link.concepts.add(concept)
        concept = Concept.obects.get(bundle.obj.concepts[1])
        new_link.concepts.add(concept)
        new_link.save()
        
        return bundle

    def obj_update(self, bundle, **kwargs):
        #updates an object, needs more coding
        return self.obj_create(bundle, **kwargs)

    def obj_delete_list(self, bundle, **kwargs):
        results = Concept.objects.all()

        for result in results:
            result.delete()


    def obj_delete(self, bundle, **kwargs):
        result = Concept.objects.filter(label=kwargs['pk'])

        result.delete()

    def rollback(self, bundles):
        pass

    def dehydrate_concepts(self, bundle):
        concepts = []
        for key in bundle.data:
            sys.stderr.write(str(bundle.data[key])+"\n")
        return bundle
    
        
