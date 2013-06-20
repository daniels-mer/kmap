"""
    Template for kmap project's test files
    
    NAME: Name of the test file
    
    DESCRIPTION: Description of the test cases
    
    To run tests : nosetests test_name.py
    Verobse (-v) : nosetests -v test_name.py
    NoCapture (-s) : nosetests -s test_name.py
"""


def setup_module(module):
    """
        If the same setup is needed for all the tests 
    """

class TestFile:

    def setup(self):
        """
            Initialize setup before each test is run
        """

    def test_01_description(self):
        """
            Class tested
            Method Tested
            Description
        """


    def test_02_description(self):
        """
            Function Tested
            Description
        """
        
    def teardown(self):
        """
            Delete data
        """

def teardown_module(module):
    """
        Delete module data
    """