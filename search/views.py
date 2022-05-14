from django.shortcuts import render

# Create your views here.

from .search import lookup,lookup_ned


def search_view(request):
    # https://www.google.com/search?q=ffff&oq=ffff&aqs=chrome..69i57j46j0l6.824j0j7&sourceid=chrome&ie=UTF-8
    query_params = request.GET
    q = query_params.get('q')

    context = {}

    if q is not None:
        results, msg = lookup(q)
        context['results'] = results
        context['query'] = q
        context['msg'] =msg
    return render(request, 'search.html', context)


def search_ned_view(request):
    # https://www.google.com/search?q=ffff&oq=ffff&aqs=chrome..69i57j46j0l6.824j0j7&sourceid=chrome&ie=UTF-8
    query_params = request.GET
    q = query_params.get('q')

    context = {}

    if q is not None:
        results, msg = lookup_ned(q)
        context['results'] = results
        context['query'] = q
        context['msg'] =msg
    return render(request, 'ned_search.html', context)