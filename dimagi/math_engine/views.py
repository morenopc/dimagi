from operator import mul

from django.views.generic import View

from braces.views import JSONResponseMixin
from django.utils import simplejson


class MathEngineView(JSONResponseMixin, View):

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
