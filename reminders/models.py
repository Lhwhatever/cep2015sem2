from django.db import models
import django.utils

class BaseModel(models.Model):
    last_modified = models.DateTimeField("Last Modified", auto_now_add=True)
    
    class Meta:
        abstract = True
        get_latest_by = ("last_modified",)

# Create your models here.
class Task(BaseModel):
    title = models.CharField("Task Title", max_length=255)
    content = models.TextField("Task Description")
    date_end = models.DateTimeField("Date of Completion")
    
    def __str__(self):
        return self.title
        
    class Meta(BaseModel.Meta):
        ordering = ("date_end",)
        verbose_name = "task"
        verbose_name_plural = "tasks"