# -*- coding: utf-8 -*-

"""
    Template for the project kmap.
    
    NAME: Name of the module/tool
    
    DESCRIPTION: Description of the module/tool
    
    If developing a command-line tool specify the arguments and options
    
    SYNOPSIS:
    
    python tool.py FILE [OPTIONS]
    
    OPTIONS:

    -v/--verbose: Prints more information

    OUTPUT:
    
    File with the results.

"""

# IMPORTS

# CONSTANTS


# INTERNAL FUNCTIONS

def __private_function(self, param):
    """
        Function description
        
        @param param: Parameter description.
        @type param: Parameter type.
        
        @return: Return value.
        @rtype: Return type.
                
        @raise error: If the function raises an exception.
    """

# PUBLIC FUNCTIONS

def function(self, param):
    """
        Function description
        
        @param param: Parameter description.
        @type param: Parameter type.
        
        @return: Return value.
        @rtype: Return type.
        
        @raise error: If the function raises an exception.
    """




# CLASS

class FirstClass:
    """
        Class description
    """

    def __init__(self, param):
        """
            Instantiation  function
            
            @param param: Parameter description.
            @type param: Parameter type.
        """
        # INSTANCE VARIABLES
        self.param = param

        """
            @ivar: Instance variable description.
            @type: Instance variable type.
        """
        self.dict = {}
        

    # PUBLIC METHODS
    def method(self, param1):
        """
            Function description
        
            @param param: Parameter description.
            @type param: Parameter type.
            
            @return: Return value.
            @rtype: Return type.
            
            @raise error: If the function raises an exception.
        """

    # INTERNAL FUNCTIONS
    def __private_method(self, param1):
        """
           Function description
        
            @param param: Parameter description.
            @type param: Parameter type.
            
            @return: Return value.
            @rtype: Return type.
            
            @raise error: If the function raises an exception.
        """





# EXCEPTION CLASS

class CustomError(Exception):
    """
        Exception class description
    """
    
    
    def __init__(self, param):
        """
            Instantiation  function

            @param param: Parameter description.
            @type param: Parameter type.
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


