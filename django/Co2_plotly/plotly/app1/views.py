from django.shortcuts import render
from .models import Co2Trend
import plotly.express as px
from .forms import DateForm
# Create your views here.

def chart(request):
    co2 = Co2Trend.objects.all()
    start = request.GET.get('start')
    end = request.GET.get('end')

    if start:
        co2 = Co2Trend.filter(date__gte=start)
    if end:
        co2 = Co2Trend.filter(date__gte=end)

    fig = px.line(
        x=[c.date for c in co2],
        y=[c.average for c in co2],
        title="CO2 PPM",
        labels={'x': 'Date', 'y': 'CO2 PPM'}
    )

    fig.update_layout(
        title={'font_size':22,
               'xanchor': 'center',
               'x':0.5}
    )
    
    chart = fig.to_html
    context = {'chart': chart, 'form':DateForm()}
    return render(request, 'app1/main.html', context)
