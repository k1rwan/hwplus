import graphene
import data.schema

class Query(data.schema.Query, graphene.ObjectType):
    pass

class Mutations(graphene.ObjectType):
    create_user = data.schema.CreateUser.Field()
    edit_user = data.schema.EditUser.Field()
    create_course = data.schema.CreateCourse.Field()
    edit_course = data.schema.EditCourse.Field()
    create_assignment = data.schema.CreateAssignment.Field()
    edit_assignment = data.schema.EditAssignment.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)