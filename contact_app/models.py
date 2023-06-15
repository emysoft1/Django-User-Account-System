from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.department_name


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.subject