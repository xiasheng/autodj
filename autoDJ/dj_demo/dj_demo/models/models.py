

from django.db import models
import time

def Now():
    return int(time.time())

class Demo(models.Model):
    user_id = models.IntegerField(primary_key=True)
    dev_id = models.CharField(max_length=128)
    mac = models.CharField(max_length=32)
    token = models.CharField(max_length=128)
    password = models.CharField(max_length=128, null=True)
    nickname = models.CharField(max_length=64, default='')
    type = models.CharField(max_length=32, null=True)
    is_test = models.BooleanField(default=False)
    is_enable = models.BooleanField(default=True)
    time_created = models.IntegerField(default=Now)
    
    def toJSON(self):
        r = {}
        r['id'] = str(self.user_id)
        r['mac'] = self.mac
        r['token'] = self.token
        r['nickName'] = self.nickname
        return r
