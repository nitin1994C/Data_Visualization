from django.shortcuts import render
from .models import Sales
import plotly.express as px
import matplotlib.pyplot as plt

# Create your views here.

def main_view(request):
    qs = Sales.objects.all()
    print(qs)
    x = [x.items for x in qs]
    y = [y.price for y in qs]
    print(y)

    chart = plt.plot(x,y)
    chart = chart.to_html()
    return render(request, 'app1/main.html', {'chart': chart})

