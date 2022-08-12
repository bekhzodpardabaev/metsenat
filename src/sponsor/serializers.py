from rest_framework import serializers
from .models import Sponsor, SponsorIntroduction, SponsorsToTheStudent, Student, University


class SponsorSerializer(serializers.ModelSerializer):
    choice = serializers.ChoiceField(choices=[
        'natural_person',
        'legal_entity'
    ])

    class Meta:
        model = Sponsor
        fields = ('choice', 'name', 'phone_number', 'payment', 'organization')


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('name',)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'phone_number', 'university', 'degree', 'contract')


class SponsorsToTheStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorsToTheStudent
        fields = ('student', 'sponsor', 'allocated_sum')


class SponsorsListSerializer(serializers.ModelSerializer):
    spent_sum = serializers.IntegerField()
    date = serializers.DateField()
    status = serializers.CharField()

    class Meta:
        model = Sponsor
        fields = ('name', 'phone_number', 'payment', 'spent_sum', 'date', 'status')


class StudentsListSerializer(serializers.ModelSerializer):
    allocated_sum = serializers.IntegerField()

    class Meta:
        model = Student
        fields = ('name', 'degree', 'university', 'allocated_sum', 'contract')


class StudentAboutSerializer(serializers.ModelSerializer):
    allocated_sum = serializers.IntegerField()

    class Meta:
        model = Student
        fields = ('name', 'phone_number', 'university', 'degree', 'allocated_sum', 'contract')


class SponsorsOfStudentSerializer(serializers.ModelSerializer):
    allocated_sum = serializers.IntegerField()

    class Meta:
        model = Sponsor
        fields = ('name', 'allocated_sum')


class SponsorAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorsToTheStudent
        fields = ('sponsor', 'allocated_sum')


class SponsorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorsToTheStudent
        fields = ('sponsor', 'allocated_sum')
