from django.db.models import F, Sum
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sponsor, SponsorsToTheStudent, Student, University
from .serializers import SponsorSerializer, SponsorsListSerializer, StudentsListSerializer, StudentSerializer, \
    UniversitySerializer, StudentAboutSerializer, SponsorsOfStudentSerializer, SponsorAddSerializer, \
    SponsorDetailSerializer
from django_filters import rest_framework as filters


class SponsorCreateView(generics.CreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class SponsorsListView(generics.ListAPIView):
    serializer_class = SponsorsListSerializer
    queryset = Sponsor.objects.prefetch_related('sponsor_introduction').annotate(
        date=F('sponsor_introduction__date'),
        status=F('sponsor_introduction__status')
    ).prefetch_related('sponsors_student').annotate(spent_sum=Sum('sponsors_student__allocated_sum'))
    # queryset = SponsorIntroduction.objects.select_related("sponsor").annotate(
    #         name=F("sponsor__name"),
    #         phone_number=F("sponsor__phone_number"),
    #         payment=F("sponsor__payment")
    # )
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('sponsor_introduction__status', 'payment', 'sponsor_introduction__date')


class SponsorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    lookup_url_kwarg = 'id'


class UniversityListCreateView(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class UniversityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    lookup_url_kwarg = 'id'


class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_url_kwarg = 'id'


class StudentListView(generics.ListAPIView):
    serializer_class = StudentsListSerializer

    def get_queryset(self):
        student = Student.objects.prefetch_related('sponsors_student').annotate(
            allocated_sum=Sum('sponsors_student__allocated_sum')
        )
        return student
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('degree', 'university')


class StudentAboutView(generics.RetrieveAPIView):
    serializer_class = StudentAboutSerializer
    queryset = Student.objects.prefetch_related('sponsors_student').annotate(
            allocated_sum=Sum('sponsors_student__allocated_sum')
    )
    lookup_url_kwarg = 'id'


class SponsorsOfStudentView(generics.ListAPIView):
    serializer_class = SponsorsOfStudentSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        queryset = Sponsor.objects.prefetch_related('sponsors_student').filter(sponsors_student__student=id).annotate(
            allocated_sum=F('sponsors_student__allocated_sum')
        )
        return queryset


class SponsorsAddStudentView(generics.CreateAPIView):
    serializer_class = SponsorAddSerializer
    queryset = SponsorsToTheStudent.objects.all()

    def perform_create(self, serializer):
        pk = Student.objects.get(id=self.kwargs['id'])
        serializer.validated_data['student'] = pk
        serializer.save()


class SponsorsOfStudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SponsorDetailSerializer
    queryset = SponsorsToTheStudent.objects.all()
    lookup_url_kwarg = 'id'


class DashboardView(APIView):
    def get(self, request):
        student = Student.objects.all()
        all_request_sum = 0
        for i in student:
            all_request_sum += i.contract
        sponsor_of_student = SponsorsToTheStudent.objects.all()
        all_paid_sum = 0
        for i in sponsor_of_student:
            all_paid_sum += i.allocated_sum
        sponsor = Sponsor.objects.all()
        all_student = 0
        all_sponsor = 0
        for i in sponsor:
            all_sponsor += 1
        for i in student:
            all_student += 1

        return Response({'all_request_sum': all_request_sum,
                         'all_paid_sum': all_paid_sum,
                         'must_be_paid': all_request_sum-all_paid_sum,
                         'all_student': all_student,
                         'all_sponsor': all_sponsor})
