from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader

# Create your views here.


def home_view(request):
    """."""
    # template = loader.get_template('imagersite/base.html')
    # response_body = template.render()
    # return HttpResponse(response_body)
    return render(request, 'imagersite/base.html', {})
