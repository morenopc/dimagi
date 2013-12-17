from django.views.generic import View


from braces.views import JSONResponseMixin
# from braces.views import CsrfExemptMixin, JsonRequestResponseMixin


class MathEngineView(JSONResponseMixin, View):

    content_type = 'application/javascript'
    json_dumps_kwargs = {'indent': 2}

    def get(self, request, *args, **kwargs):

        values = request.GET.get('values')

        context_dict = {'values': values}

        return self.render_json_response(context_dict)
