from data.models import User
from rest_framework import serializers

from data import models


# class HWFUserProfileSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = models.HWFUserProfile

class UserSerializer(serializers.ModelSerializer):
    
    bupt_id=serializers.CharField(required=False)
    class_number=serializers.CharField(required=False)
    is_active=serializers.BooleanField(read_only=True,required=False)
    date_joined=serializers.DateTimeField(read_only=True,required=False)

    def create(self,validated_data):
        vd=validated_data
        username,password,email,phone,name,wechat,usertype,gender=vd['username'],vd['password'],vd['email'],vd['phone'],vd['name'],vd['wechat'],vd['usertype'],vd['gender']
        user=None
        try:
            bupt_id=vd['bupt_id']
            class_number=vd['class_number']
            user=User.objects.create(usertype=usertype,gender=gender,username=username,email=email,bupt_id=bupt_id,phone=phone,class_number=class_number,name=name,wechat=wechat,is_active=False)
        except KeyError:
            pass
        user=User.objects.create(usertype=usertype,gender=gender,username=username,email=email,phone=phone,class_number="000",name=name,wechat=wechat,is_active=False)
        user.set_password(password)
        user.save()
        return user
    class Meta:
        model = User
        fields=('is_active','date_joined','username','name','gender','usertype','password','bupt_id','class_number','email','phone','wechat')

class HWFCourseClassSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.HWFCourseClass
        fields='__all__'

class HWFAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.HWFAssignment
        fields='__all__'

class HWFSupportFileExtensionSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.HWFSupportFileExtension
        fields='__all__'

class HWFFileSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.HWFFile
        fields='__all__'

class HWFSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.HWFSubmission
        fields='__all__'

class HWFQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.HWFQuestion
        fields='__all__'

class HWFAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.HWFAnswer
        fields='__all__'

class HWFTextAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.HWFTextAnswer
        fields='__all__'

class HWFSelectAnswerValueSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.HWFSelectAnswerValue
        fields='__all__'

class HWFSelectAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.HWFSelectAnswer
        fields='__all__'

class HWFFileAnswerValueSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.HWFFileAnswerValue
        fields='__all__'

class HWFFileAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.HWFFileAnswer
        fields='__all__'

class HWFSelectQuestion(serializers.ModelSerializer):
    class Meta:
        model=models.HWFSelectQuestion
        fields='__all__'

class HWFSelectQuestionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.HWFSelectQuestionChoice
        fields='__all__'

class HWFFileQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.HWFFileQuestion
        fields='__all__'

class HWFReviewTagSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.HWFReviewTag
        fields='__all__'

class HWFReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.HWFReview
        fields='__all__'

# class HWFMessage(serializers.ModelSerializer):
#     class Meta:
#         model=models.HWFMessage