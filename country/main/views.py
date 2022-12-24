from rest_framework.response import Response
from rest_framework.decorators import api_view

from .wbscrap import result

import json


# Create your views here.
@api_view(['GET'])
def home(request, countryname):
    if request.method == "GET":
        
        country= countryname
        final_dict= result(country)
        print(final_dict)
        return Response(json.loads(json.dumps(final_dict)))
        return(Response('Search for a Country'))


