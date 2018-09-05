# -*- coding: utf-8 -*-
from graphene_django.views import *
from django.http import HttpResponseForbidden
from data.user_views import token
from data import encrypt
from data import models

# 使得GraphQL的访问需要验证token

class BetterGraphQLView(GraphQLView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        # return super().dispatch(request, *args, **kwargs)
        tk = request.META.get('HTTP_TOKEN','')
        try: 
            token.confirm_validate_token(tk)
            return super().dispatch(request, *args, **kwargs)
        except:
            try:
                hs = encrypt.getHash(tk)
                models.User.objects.get(wechat=hs)
                return super().dispatch(request, *args, **kwargs)
            except:
                return HttpResponseForbidden('{"error":"forbidden"}',content_type="application/json")

