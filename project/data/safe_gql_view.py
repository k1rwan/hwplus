from graphene_django.views import *
from django.http import HttpResponseForbidden
from data.user_views import token

class BetterGraphQLView(GraphQLView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        tk = request.META.get('HTTP_TOKEN','')
        try: 
            token.confirm_validate_token(tk)
            return super().dispatch(request, *args, **kwargs)
        except:
            return HttpResponseForbidden('{"error":"forbidden"}',content_type="application/json")
