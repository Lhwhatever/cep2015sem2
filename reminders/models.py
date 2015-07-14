from django.db import models
from django.utils import timezone
import datetime


class BaseModel(models.Model):
    last_modified = models.DateTimeField("Last Modified", auto_now_add=True)
    
    class Meta:
        abstract = True
        get_latest_by = ("last_modified",)


class Task(BaseModel):
    """
    A task to be completed by the user.
    """
    title = models.CharField("Task Title", max_length=255)
    content = models.TextField("Task Description")
    date_end = models.DateTimeField("Target Date of Completion")
    is_completed = models.BooleanField("Completed")
    time_left = None

    _class_status = ["default", "warning", "danger", "success"]
    _advice_status = ["This task is not complete yet.", "This task should be completed within 24 hours!",
                      "This task is overdue!", "This task is complete! You can delete it now."]

    def __str__(self):
        return self.title
        
    class Meta(BaseModel.Meta):
        ordering = ("date_end",)
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def get_status_ref_id(self):
        """
        :return: ID for internal use regarding the completion status of the task.
        """
        return -1 if self.is_completed else \
            (0 if timezone.now() + datetime.timedelta(days=1) <= self.date_end else(
                1 if timezone.now() < self.date_end else 2
            ))

    @property
    def get_associated_class(self):
        """
        :return: Appropriate bootstrap class for formatting the task based on completion status.
        """
        return Task._class_status[self.get_status_ref_id()]

    @property
    def get_associated_advice(self):
        """
        :return: Appropriate tooltips for the task based on completion status.
        """
        return Task._advice_status[self.get_status_ref_id()]
