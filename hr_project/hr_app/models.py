from django.db import models
from mongoengine import Document, IntField, StringField, DateField, DictField

# Create your models here.


# ✅ PostgreSQL Model (No Change)
class Employee(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    DEPARTMENT_CHOICES = [('IT', 'IT'), ('HR', 'HR'), ('Finance', 'Finance'), ('Sales', 'Sales'), ('AI','AI')]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.department}"


# ✅ MongoDB Model (Using `mongoengine`)
class PerformanceReview(Document):
    employee_id = IntField(required=True)
    review_date = DateField(required=True)
    reviewer = StringField(max_length=100, required=True)
    rating = IntField(min_value=1, max_value=5, required=True)
    comments = StringField()
    goals = DictField()  # Stores JSON-like data

    meta = {'collection': 'performance_reviews'}
