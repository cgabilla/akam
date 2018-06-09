from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'i-asiv-backend-pyramid'}

###
CITIES = {
    'paris': {
        'name': 'Paris',
        'population': '2,234,105'
    },
    'sf': {
        'name': 'San Francisco',
        'population': '812,826'
    }
}

@view_config(route_name='city', renderer='json')
def get_city(request):
    name = request.matchdict['name']
    return CITIES[name]

@view_config(route_name='cities', renderer='json')
def list_cities(request):
    return CITIES
