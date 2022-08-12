from datetime import datetime
from django.db import models


class Sponsor(models.Model):
    class Person(models.Choices):
        natural_person = "Natural person"
        legal_entity = "Legal entity"
    choice = models.TextField(choices=Person.choices)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    payment = models.PositiveIntegerField()
    organization = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class University(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Student(models.Model):
    degree_choice = [
        ("bachelor", "Bachelor"),
        ("master", "Master")
    ]
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    university = models.ForeignKey('University', on_delete=models.PROTECT)
    degree = models.TextField(choices=degree_choice)
    contract = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class SponsorIntroduction(models.Model):
    status_choice = [
        ('new', 'New'),
        ('moderation', 'Moderation'),
        ('approved', 'Approved'),
        ('canceled', 'Canceled')
    ]
    sponsor = models.OneToOneField('Sponsor', on_delete=models.CASCADE, related_name='sponsor_introduction')
    date = models.DateField(default=datetime.now)
    status = models.TextField(choices=status_choice)

    def __str__(self):
        return f"{self.sponsor.name} {self.status}"


class SponsorsToTheStudent(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='sponsors_student')
    sponsor = models.ForeignKey('Sponsor', on_delete=models.PROTECT, related_name='sponsors_student')
    allocated_sum = models.PositiveIntegerField()

    class Meta:
        unique_together = ('student', 'sponsor')

    def __str__(self):
        return f"student:{self.student.name} sponsor:{self.sponsor.name}"


