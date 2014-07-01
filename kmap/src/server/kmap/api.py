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
from neo4jrestclient.client import GraphDatabase, Node
from django.core.exceptions import ObjectDoesNotExist
from tastypie.resources import Resource
from tastypie.authorization import Authorization
from tastypie.bundle import Bundle
from tastypie.exceptions import NotFound, BadRequest
from tastypie import fields
from kmap.models import Concept, Link
from kmap.serializers import ConceptJSONSerializer
from kmap.timer import Timer

class ConceptResource(Resource):
    # Just like a Django ``Form`` or ``Model``, we're defining all the
    # fields we're going to handle with the API here.
    
    label = fields.CharField(attribute='label', unique=True)
    description = fields.CharField(attribute='description', null=True)
    weight = fields.IntegerField(attribute='weight', null=True, default=1)
    
    links = fields.ToManyField(to='kmap.api.LinkResource', attribute="links", 
                               null=True, blank=True)
    

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
        if "neighbor" in request.GET:
            concept = Concept.objects.filter(label__iexact=request.GET["neighbor"])[0]

            results = concept.node_links(request.GET.get("type", None))

        elif "search" in request.GET:
            pass
            ""
        else:
            #Get random node, return node + x neigbours
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

    def obj_create(self, bundle, **kwargs): #POST
        #creates an object
        sys.stderr.write("obj_create is called \n")
        bundle.obj = Concept()
        bundle = self.full_hydrate(bundle)
        try:
            new_concept = Concept.objects.create(label=bundle.obj.label,
                                             description=bundle.obj.description,
                                             weight=bundle.obj.weight)
        
            new_concept.save()
        except Exception:
            raise BadRequest
        return bundle

    def obj_update(self, bundle, **kwargs): #PUT
        #updates an object, needs more coding
        sys.stderr.write("obj_update is called \n")
        try:
            concept = Concept.objects.get(label=kwargs['pk'])
            bundle.obj = Concept()
            bundle = self.full_hydrate(bundle)
            if bundle.obj.label is not None:
                concept.label = bundle.obj.label
            if bundle.obj.description is not None:
                concept.description = bundle.obj.description
            if bundle.obj.weight is not None:
                concept.weight = bundle.obj.weight
            concept.save()
        except ObjectDoesNotExist:
            return self.obj_create(bundle, **kwargs)

    def obj_delete_list(self, bundle, **kwargs):
        results = Concept.objects.all()

        for result in results:
            result.delete()

    def obj_delete(self, bundle, **kwargs):
        try:
            result = Concept.objects.filter(label=kwargs['pk'])
            result.delete()
        except ObjectDoesNotExist:
            raise NotFound

    def rollback(self, bundles):
        pass
    
    def dehydrate(self, bundle):
        links = []
        gdb = GraphDatabase("http://localhost:7474/db/data/")
        query = """START a = node:`kmap-Concept`(label = "%s")
                 MATCH a<-[:concepts]-b-[:concepts]->c
                 RETURN b, c;
                """ % bundle.data["label"]
        data = gdb.query(q=query, returns=(Node, Node))
        for datum in data:
            links.append({"type" : datum[0]["type"], 
                          "label" : datum[1]["label"]})

        bundle.data["links"] = links
        return bundle

class LinkResource(Resource):
    # Just like a Django ``Form`` or ``Model``, we're defining all the
    # fields we're going to handle with the API here.
#     id = fields.IntegerField(attribute='id', unique=True)
    
    link_type = fields.CharField(attribute='type', unique=False)
    weight = fields.IntegerField(attribute='weight', null=True, default=1)

    concepts = fields.ToManyField(to='kmap.api.ConceptResource', 
                                  attribute="concepts", null=True, blank=True)
    
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
            kwargs['pk'] = bundle_or_obj.obj.id
        else:
            sys.stderr.write(repr(bundle_or_obj))
            kwargs['pk'] = bundle_or_obj[0].id
        
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
        sys.stderr.write("obj_get is called\n")
        object_id = kwargs['pk']
        sys.stderr.write("obj_get is called label:%s\n"%str(object_id))
        resource = Link.objects.filter(id=object_id)
        sys.stderr.write("obj_get is called resource:%s\n"%type(resource))
        sys.stderr.write("obj_get is called prueba %s\n"% type(self._meta.object_class()))
        return resource[0]
        
    def obj_create(self, bundle, **kwargs):
        #creates an object
        sys.stderr.write("obj_create is called \n")
        bundle.obj = Link()
        bundle = self.full_hydrate(bundle)
        sys.stderr.write(repr(bundle.obj.concepts.all()))
        sys.stderr.write(str(bundle.obj.concepts.all()))
        concept0 = Concept.objects.get(label=bundle.obj.concepts.all()[0])
        concept1 = Concept.objects.get(label=bundle.obj.concepts.all()[1])
        try:
            new_link = Link.objects.create(type=bundle.obj.type)
            new_link.concepts.add(concept0)
            new_link.concepts.add(concept1)
            new_link.weight = bundle.obj.weight
            new_link.save()
        except Exception as exc:
            sys.stderr.write(str(exc))
            return BadRequest
        
        return bundle

    def obj_update(self, bundle, **kwargs):
        #updates an object, needs more coding
        try:
            link = Link.objects.get(id=kwargs['pk'])
            bundle.obj = Link()
            bundle = self.full_hydrate(bundle)
            if bundle.obj.type is not None:
                link.type = bundle.obj.type
            if bundle.obj.concepts[0] is not None:
                concept = Concept.objects.get(label=bundle.obj.concepts.all()[0])
                link.concepts[0] = concept
            if bundle.obj.concepts[1] is not None:
                concept = Concept.objects.get(label=bundle.obj.concepts.all()[1])
                link.concepts[1] = concept
            if bundle.obj.weight is not None:
                link.weight = bundle.obj.weight
                
            link.save()
        except ObjectDoesNotExist:
            return self.obj_create(bundle, **kwargs)

    def obj_delete_list(self, bundle, **kwargs):
        results = Link.objects.all()

        for result in results:
            result.delete()


    def obj_delete(self, bundle, **kwargs):
        try:
            result = Link.objects.get(id=kwargs['pk'])        
            result.delete()
        except ObjectDoesNotExist:
            raise NotFound
        
    def rollback(self, bundles):
        pass

    def dehydrate(self, bundle):
        
        for key in bundle.data:
            sys.stderr.write(str(bundle.data[key])+"\n")
        return bundle
    
    def hydrate(self, bundle):
        
        if len(bundle.data["concepts"]) != 2:
            raise BadRequest
        concepts = []
        if bundle.data["concepts"][0]:
            if bundle.data["concepts"][0].split("/")[-1]:
                concepts.append(bundle.data["concepts"][0].split("/")[-1])
            else:
                concepts.append(bundle.data["concepts"][0].split("/")[-2])
        else:
            concepts.append('')
            
        if bundle.data["concepts"][1]:
            if bundle.data["concepts"][1].split("/")[-1]:
                concepts.append(bundle.data["concepts"][1].split("/")[-1])
            else:
                concepts.append(bundle.data["concepts"][1].split("/")[-2])
        else:
            concepts.append('')
            
        setattr(bundle.obj, "concepts", concepts)
        return bundle
        
