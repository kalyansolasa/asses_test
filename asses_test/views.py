from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
import pandas as pd
#from matplotlib import pyplot as plt

def index(request):
    if "GET" == request.method:
        return render(request, 'home.html', {})
    else:
        excel_file = request.FILES["excel_file"]
        print(excel_file)

        # you may put validations here to check extension or file size


        return render(request, 'home.html', {'file_name':'test1.png'})
