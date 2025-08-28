from django.db import models

class Subject(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  image = models.URLField(max_length=500)
  objective = models.TextField()
  audience = models.TextField()
  
  class Meta:
    db_table = 'tb_subjects'

class Curriculum(models.Model):
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='curriculums')
  period = models.IntegerField()
  topic = models.CharField(max_length=100)
  task = models.CharField(max_length=100)
  content = models.TextField()
  
  class Meta:
    db_table = 'tb_curriculums'
