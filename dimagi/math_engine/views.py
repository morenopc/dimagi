from operator import mul

from django.views.generic import View

from braces.views import JSONResponseMixin
from django.utils import simplejson

from .models import MathEngineHistory


class MathEngineView(JSONResponseMixin, View):
    """ Web Development 1) Math Engine """
    
    content_type = 'application/javascript'
    json_dumps_kwargs = {'indent': 2}

    def get(self, request, *args, **kwargs):

        values = request.GET.get('values')
        values_list = map(int, values[1:-1].split(', '))
        context_dict = {
            'sum': sum(values_list),
            'product': reduce(mul, values_list)
        }

        return self.render_json_response(context_dict)


class MathEngineChallengeView(JSONResponseMixin, View):
    """ Web Development 2) (Challenge) """

    content_type = 'application/javascript'
    json_dumps_kwargs = {'indent': 2}

    def get(self, request, *args, **kwargs):

        rds = request.GET.get('records', 1)
        values = request.GET.get('values')
        
        values_list = map(int, values[1:-1].split(', '))

        MathEngineHistory.objects.create(
            ip=request.META.get('REMOTE_ADDR'),
            values=values,
            sum=sum(values_list),
            product=reduce(mul, values_list))

        context_dict = [{
            'ip': result.ip,
            'timestamp': result.created,
            'values': result.values,
            'sum': result.sum,
            'product': result.product
        } for result in MathEngineHistory.objects.all(
            ).order_by('-created')[:rds]]

        return self.render_json_response(context_dict)
