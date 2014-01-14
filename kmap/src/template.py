# -*- coding: utf-8 -*-

"""
    :mod:`template` -- Template for python modules
    ===================================
    
    .. module:: src.template
          :synopsis: template for python modules.
    .. moduleauthor:: Daniel Santonja
        
    :License: GPL (https://gnu.org/licenses/gpl.html)
    
    :Date last change:
    
    :Version:
"""

# IMPORTS

# CONSTANTS


# INTERNAL FUNCTIONS

def __private_function(param):
    """
        ..function :: __private_function(param)
        
        Description of the function
        :param param: Parameter description.
        :type param: Parameter type.
        
        :returns: Return value
        :rtype: Return type.
                
        :raises: If the function raises an exception.
    """

# PUBLIC FUNCTIONS

def function(self, param):
    """
        ..function :: function(param)
        
        Description of the function
        :param param: Parameter description.
        :type param: Parameter type.
        
        :returns: Return value
        :rtype: Return type.
                
        :raises: If the function raises an exception
    """




# CLASS

class FirstClass:
    """
        ..class:: FirstClass
        
        Class description
    """

    def __init__(self, param, optional=None):
        """
            ..method::__init__(param [, optional])
            Instantiation method
            
            :param param: Parameter description.
            :type param: Parameter type.
            :param optional: Parameter description.
            :type optional: Parameter type.
        """
        # INSTANCE VARIABLES
        self.param = param

        """
            ..attribute: Instance variable description.
        """
        self.dict = {}
        

    # PUBLIC METHODS
    def method(self, param1):
        """
            ..method::method(param1)
            
            Method description
            
            :param param1: Parameter description.
            :type param1: Parameter type.
            
            :returns: Return value
            :rtype: Return type.
            
            :raises: If the function raises an exception.
        """

    # INTERNAL FUNCTIONS
    def __private_method(self, param1):
        """
           ..method::__private_method(param1)
            
            Method description
            
            :param param1: Parameter description.
            :type param1: Parameter type.
            
            :returns: Return value
            :rtype: Return type.
            
            :raises: If the function raises an exception.
        """


# EXCEPTION CLASS

class CustomError(Exception):
    """
        ..exception:CustomError
        
        Exception class description
    """
    
    
    def __init__(self, param):
        """
            ..method::__init__(param)
            Instantiation method
            
            :param param: Parameter description.
            :type param: Parameter type.
        """
        self.param = param
    
    # TO STRING FUNCTION
    def __str__(self):
        """
            Function description
        """
        return "CustomError " + str(self.param)
    

# MAIN
def main(self):
    """
        Main function description
    """
    
# If the program is run directly or passed as argument to the Python 
# interpreter, then we call main function
if __name__ == "__main__":
    main()


