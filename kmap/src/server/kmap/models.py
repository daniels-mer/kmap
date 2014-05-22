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
    weight = models.IntegerProperty(unique=False, null=True, default=1)

#     links = models.Relationship('Link', rel_type='links')
#     
    def nodelinks(self, link_type=None):
        if link_type:
            return [link.opposite(self.label) for link in self.links.all() if link.type==link_type]
        else:
            return [link.opposite(self.label) for link in self.links.all()]


class Link(models.NodeModel):
    """
        ..class:: Link

        This class is a workaround to provide flexible links in neo4django, 
        it connects 2 nodes
    """
#     id = models.IntegerProperty(unique=True, indexed=True)

    type = models.StringProperty(unique=False, indexed=True)

    concepts = models.Relationship('Concept', rel_type='concepts', related_name="links")
    weight = models.IntegerProperty(unique=False, null=True, default=1)
    
    def opposite(self, label):
        if self.concepts.all()[0].label == label:
            return self.concepts.all()[1]
        else:
            return self.concepts.all()[0]

    def __str__(self):
        if self.concepts.all() == 2:
            return "%s <- %s ->%s"(self.concepts.all()[0], self.type, self.concepts.all()[1])
        else:
            return "id:%d\t type:%s" % (self.id, self.type)

