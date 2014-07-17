# -*- coding: utf-8 -*-

"""
    :mod:`serializers` -- 
    ===================================
    
    .. module:: src.server.kmap
          :synopsis: Classes to handle json to model conversion and vice versa.
    .. moduleauthor:: Daniel Santonja
        
    :License: GPL (https://gnu.org/licenses/gpl.html)
    
    :Date last change:
    
    :Version:
"""
import json
from django.core.serializers.json import DjangoJSONEncoder
from tastypie.serializers import Serializer
import sys

class ConceptJSONSerializer(Serializer):
    """
        ..class:: Concept
        
        This class improves the json-model transformation for the model Concept 
    """
    def to_json(self, data, options=None):
        """
            ..method::to_json(data, options=None):
            
            Given concept data it returns it json representation
            
            :param data: Concept data.
            :type data: dict.
            :param data: Options to parse the json.
            :type data: dict.
            
            :returns: The json
            :rtype: String. 
        """
        options = options or {}
        data = self.to_simple(data, options)

        sys.stderr.write(str(data)+"\n")
        return json.dumps(data, cls=DjangoJSONEncoder, sort_keys=True)

    def from_json(self, content):
        """
            ..method::from_json(content):
            
            Given a json content it returns a python dictionary
            
            :param content: Json data.
            :type data: String.
            
            :returns: The data as an object
            :rtype: dict. 
        """
        data = json.loads(content)

        return data
    
class LinkJSONSerializer(Serializer):
    """
        ..class:: Concept
        
        This class improves the json-model transformation for the model Link 
    """
    def to_json(self, data, options=None):
        """
            ..method::to_json(data, options=None):
            
            Given concept data it returns it json representation
            
            :param data: Concept data.
            :type data: dict.
            :param data: Options to parse the json.
            :type data: dict.
            
            :returns: The json
            :rtype: String. 
        """
        options = options or {}

        data = self.to_simple(data, options)

        return json.dumps(data, cls=DjangoJSONEncoder, sort_keys=True)

    def from_json(self, content):
        """
            ..method::from_json(content):
            
            Given a json content it returns a python dictionary
            
            :param content: Json data.
            :type data: String.
            
            :returns: The data as an object
            :rtype: dict. 
        """
        data = json.loads(content)


        return data