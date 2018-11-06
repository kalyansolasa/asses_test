from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from accounts.models import FileProcess
from asses_test.settings import STATICFILES_ROOT
import pandas as pd
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import os

#from matplotlib import pyplot as plt

def index(request):
    if "GET" == request.method:
        return render(request, 'home.html', {})
    else:
        myfile = request.FILES["excel_file"]
        fs = FileSystemStorage()
        # save with random name if file name is already exists
        filename = fs.save(os.path.join(STATICFILES_ROOT,myfile.name), myfile)
        print(fs.url(filename))
        print(myfile.name)
        print(STATICFILES_ROOT)
        df = pd.read_excel('/'+fs.url(filename))
        
        fig = plt.figure()
        plt.bar(list(df['Month ']), list(df['Sales']))
        image_name = fs.url(filename).split('/')[-1].split('.')[0]+'.png'
        image_path = os.path.join(STATICFILES_ROOT,image_name)
        fig.savefig(image_path)
        fil_model = FileProcess()
        fil_model.src_file_path = filename
        fil_model.img_name = image_name
        fil_model.save()

        return render(request, 'home.html', {'fil_model':fil_model})
