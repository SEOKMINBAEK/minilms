from django.db import models

class Subject(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  logo = models.ImageField(upload_to='subjects/', blank=True, null=True)
  image = models.ImageField(upload_to='subjects/', blank=True, null=True)
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

class Apply(models.Model):
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='applies')
  subject_title = models.CharField(max_length=100)
  region = models.CharField(max_length=50)
  frequency_type = models.CharField(max_length=50)
  frequency_count = models.IntegerField()
  class_count = models.IntegerField()
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  phone = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'tb_applies'
