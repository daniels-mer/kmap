# -*- coding: utf-8 -*-
"""
    :mod:`views` -- 
    ===================================
    
    .. module:: src.server.kmap
          :synopsis: Defines the controllers of the application.
    .. moduleauthor:: Daniel Santonja
        
    :License: GPL (https://gnu.org/licenses/gpl.html)
    
    :Date last change:
    
    :Version:
"""
from django.shortcuts import render

def index(request):
    """
        ..function::index(request)
        
        A very simple controller that returns the index page.
        
        :param request: The request made by the browser.
        :type request: hhtpRequest.
        
        :returns: The webpage
        :rtype: httpResponse.        
    """
    return render(request, "kmap/index.html", {})

def navigate(request):
    """
        ..function::navigate(request)
        
        A very simple controller that returns the navigate page.
        
        :param request: The request made by the browser.
        :type request: hhtpRequest.
        
        :returns: The webpage
        :rtype: httpResponse.        
    """
    return render(request, "kmap/navigate.html", {})