# ./data/schema.py
from data.graphql_schema.query import Query
from data.graphql_schema.mutations.give_score import GiveScore
from data.graphql_schema.mutations.edit_user import EditUser
from data.graphql_schema.mutations.edit_course import EditCourse
from data.graphql_schema.mutations.edit_assignment import EditAssignment
from data.graphql_schema.mutations.delete_assignment import DeleteAssignment
from data.graphql_schema.mutations.create_user import CreateUser
from data.graphql_schema.mutations.create_submission import CreateSubmission
from data.graphql_schema.mutations.create_course import CreateCourse
from data.graphql_schema.mutations.create_assignment import CreateAssignment
