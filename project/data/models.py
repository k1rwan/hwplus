from django.contrib.auth.models import AbstractUser
from django.db import models

# from project.settings import MEDIA_ROOT


def default_bupt_id():
    count = User.objects.all().count()
    return 'noBuptId'+str(count)


def default_phone():
    count = User.objects.all().count()
    return 'noPhone'+str(count)

# User prototype

class User(AbstractUser):
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    bupt_id = models.CharField(
        max_length=10, unique=True, default=default_bupt_id)
    name = models.TextField(default='')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11, unique=True, default=default_phone)
    gender = models.CharField(max_length=6, choices=[(
        item, item) for item in ['male', 'female']], default='male')
    usertype = models.CharField(max_length=20, choices=[(item, item) for item in [
                                'student', 'teacher', 'assistant']], default='student')
    class_number = models.CharField(max_length=10, default='noClass')
    wechat = models.TextField(default='')
    forgotten = models.BooleanField(default=False)
    url_height = models.PositiveIntegerField(default=75)
    url_width = models.PositiveIntegerField(default=75)
    useravatar = models.ImageField(
        upload_to="avatars", height_field='url_height', width_field='url_width', null=True)


class HWFCourseClass(models.Model):
    name = models.TextField()
    description = models.TextField()
    marks = models.FloatField(default=0.0)
    creator = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='creator_course')
    teaching_assistants = models.ManyToManyField(
        User, related_name='teaching_assistants_course', null=True, default=[])
    # student_representatives = models.ManyToManyField(User, related_name='student_representatives_course')
    students = models.ManyToManyField(
        User, related_name='students_course', null=True, default=[])
    join_code = models.TextField(max_length=512)

    def __unicode__(self):
        return self.name


class HWFAssignment(models.Model):
    course_class = models.ForeignKey(HWFCourseClass, on_delete=models.PROTECT)
    name = models.TextField()
    description = models.TextField()
    deadline = models.DateTimeField()

    def __unicode__(self):
        return self.name


class HWFSupportFileExtension(models.Model):
    name = models.TextField()
    extension_regex = models.TextField()


# Any uploaded file is a HWFFile
# unique by hashcode
class HWFFile(models.Model):
    extension = models.ForeignKey(
        HWFSupportFileExtension, on_delete=models.PROTECT)
    data = models.FileField()
    hashcode = models.TextField(unique=True)
    # copyright user
    initial_upload_time = models.DateTimeField(editable=False)
    initial_upload_user = models.ForeignKey(
        User, on_delete=models.PROTECT, editable=False)


# submission to an assignment
class HWFSubmission(models.Model):
    submit_time = models.DateTimeField()
    assignment = models.ForeignKey(HWFAssignment, on_delete=models.PROTECT)
    submitter = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.TextField()
    score = models.FloatField()


class HWFQuestion(models.Model):
    assignment = models.ForeignKey(HWFAssignment, on_delete=models.PROTECT)
    auto_score = models.BooleanField(default=False)
    question_text = models.TextField()
    description = models.TextField()
    score = models.FloatField()


class HWFAnswer(models.Model):
    submission = models.ForeignKey(HWFSubmission, on_delete=models.PROTECT)
    reviewed = models.BooleanField(default=False)
    score = models.FloatField(default=0)
    question = models.ForeignKey(HWFQuestion, on_delete=models.PROTECT)


class HWFTextAnswer(HWFAnswer):
    values = models.TextField()


# pre generated static values
class HWFSelectAnswerValue(models.Model):
    value = models.IntegerField(unique=True)


class HWFSelectAnswer(HWFAnswer):
    values = models.ManyToManyField(HWFSelectAnswerValue)


class HWFFileAnswerValue(models.Model):
    description = models.TextField()
    value = models.ForeignKey(HWFFile, on_delete=models.PROTECT)


class HWFFileAnswer(HWFAnswer):
    values = models.ManyToManyField(HWFFileAnswerValue)


class HWFSelectQuestion(HWFQuestion):
    is_multiple_choices = models.BooleanField(default=False)
    correct_answer = models.ForeignKey(
        HWFSelectAnswer, on_delete=models.CASCADE)

    def __init__(self, *args, **kwargs):
        self._meta.get_field('auto_score').default = True
        super(HWFQuestion, self).__init__(*args, **kwargs)


class HWFSelectQuestionChoice(models.Model):
    question = models.ForeignKey(HWFSelectQuestion, on_delete=models.PROTECT)
    text = models.TextField()
    value = models.IntegerField()


class HWFFileQuestion(HWFQuestion):
    support_extensions = models.ManyToManyField(HWFSupportFileExtension)
    values = models.ManyToManyField(HWFFile)


# mark for great, good, poor
class HWFReviewTag(models.Model):
    value = models.IntegerField()
    name = models.TextField()


class HWFReview(models.Model):
    mark_review = models.ForeignKey(HWFReviewTag, on_delete=models.PROTECT)
    reviewer = models.ForeignKey(
        User, related_name='reviewer_review', on_delete=models.PROTECT)
    text = models.TextField()
    answer = models.ForeignKey(HWFAnswer, on_delete=models.PROTECT)
    is_graph_review = models.BooleanField(default=False)
    graph_value = models.TextField()


# class HWFMessage(models.Model):
#     time = models.DateTimeField()
#     sender = models.ForeignKey(User, on_delete=models.PROTECT)
#     text = models.TextField()
#     viewed = models.BooleanField(default=False)
