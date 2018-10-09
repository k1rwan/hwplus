# -*- coding: utf-8 -*-
import graphene
from django import http
from graphene_django.types import DjangoObjectType

from data import models, serializers
from data.safe_gql_view import BetterGraphQLView
from data.user_views import token

from data import encrypt
from project import settings

from data.graphql_schema.types import *
from data.graphql_schema.inputs import *

from data.graphql_schema.query import Query

from data.graphql_schema.create_user import CreateUser
from data.graphql_schema.edit_user import EditUser
from data.graphql_schema.create_course import CreateCourse
from data.graphql_schema.edit_course import EditCourse
from data.graphql_schema.create_assignment import CreateAssignment
from data.graphql_schema.edit_assignment import EditAssignment
from data.graphql_schema.delete_assignment import DeleteAssignment
from data.graphql_schema.create_submission import CreateSubmission