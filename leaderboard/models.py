from django.db import models

class Score(models.Model):
    customer_id = models.IntegerField()
    score = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'score'


class History(models.Model):
    customer_id = models.IntegerField()
    score = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'history'