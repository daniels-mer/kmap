# -*- coding: utf-8 -*-

"""
    :mod:`models` -- Models for the database
    ===================================
    
    .. module:: src.server.kmap
          :synopsis: Classes that are modeled into the database.
    .. moduleauthor:: Daniel Santonja
        
    :License: GPL (https://gnu.org/licenses/gpl.html)
    
    :Date last change:
    
    :Version:
"""
from neo4django.db import models

class Concept(models.NodeModel):
    """
        ..class:: Concept
        
        This class translates a node from neo4j to python
        For the time being is the only class 
    """
    label = models.StringProperty(unique=True, indexed=True)
    description = models.StringProperty()

    neighbour = models.Relationship('self', rel_type='neighbour')
    

