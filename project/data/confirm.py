from itsdangerous import URLSafeTimedSerializer as utsr
import base64
import re
from project.settings import SECRET_KEY
import project.settings as settings
from django.core.mail import send_mail

DOMAIN="localhost:3000"

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
    token_confirm=Token(SECRET_KEY.encode())
    token=token_confirm.generate_validate_token(user.username)
    message="\n".join(['%s,Welcome to Homework+'%user.username,
    'Visit the following link to activate your account',
    "http://"+'/'.join([DOMAIN,'emailcheck','?token='+str(token)])
    ])
    send_mail('HomeworkPlus',message,'liadrinz@163.com',[user.email])