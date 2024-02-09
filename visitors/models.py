from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    office_location = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class VisitorLog(models.Model):
    visitor_name = models.CharField(max_length=100)
    visitor_email = models.EmailField()
    visiting_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    office_location = models.CharField(max_length=100)
    status_choices = [
        ('Waiting for Check in', 'Waiting for Check in'),
        ('Inside Building', 'Inside Building'),
        ('Checked Out', 'Checked Out')
    ]
    status = models.CharField(max_length=20, choices=status_choices)

    def __str__(self):
        return self.visitor_name
