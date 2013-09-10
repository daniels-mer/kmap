from neo4django.db import models

class Person(models.NodeModel):
    name = models.StringProperty()
    age = models.IntegerProperty()

    friends = models.Relationship('self',rel_type='friends_with')
    
class OnlinePerson(Person):
    email = models.EmailProperty()
    homepage = models.URLProperty()

class EmployedPerson(Person):
    job_title = models.StringProperty(indexed=True)

class Pet(models.NodeModel):
    owner = models.Relationship(Person,
                                rel_type='owns',
                                single=True,
                                related_name='pets'
                               )
