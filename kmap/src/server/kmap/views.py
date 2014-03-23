#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.template import Context

def index(request):
    return render(request, "kmap/index.html", {})

def navigate(request):
    return render(request, "kmap/navigate.html", {})