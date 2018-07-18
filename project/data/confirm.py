from itsdangerous import URLSafeTimedSerializer as utsr
import base64
import re
from project.settings import SECRET_KEY
import project.settings as settings
from django.core.mail import send_mail

DOMAIN="108.160.130.164:8082"

class Token():
    def __init__(self, security_key):
        self.security_key=security_key
        self.salt=base64.encodestring(security_key)
    def generate_validate_token(self,username):
        serializer=utsr(self.security_key)
        return serializer.dumps(username,self.salt)
    def confirm_validate_token(self,token,expiration=3600*24):
        serializer=utsr(self.security_key)
        return serializer.loads(token,salt=self.salt,max_age=expiration)

def send(user):
    global DOMAIN
    token_confirm=Token(SECRET_KEY)
    token=token_confirm.generate_validate_token(user.username)
    message="\n",join([u'%s,欢迎加入Homework+'%user.username,
    u'请访问以下链接，完成用户验证：',
    '/'.join([DOMAIN,'account/activate',token])
    ])
    send_mail(u'[Homework+]注册用户验证信息',message,settings.EMAIL_FROM,[user.email,])
    

    
    