import datetime
from django.test import TestCase
from facilityapp.models import *
from django.contrib.auth.models import User

class FacilityTests(TestCase):

    @classmethod
    def setUpClass(cls):
        return super().setUpClass()

    @classmethod
    def setUpTestData(cls):
        cls.facility = Facility.objects.create(facility_name='test', length='1', width='1', height='1', floor_area='2', site_area='3')
        cls.usr = User.objects.create_user(username='someperson')

    def setUp(self):
        pass

    def test_create_facility(self):
        obj = Facility.objects.create(
            facility_name = self.facility,
            length='1',
            width='1', 
            height='1', 
            floor_area='2', 
            site_area='3'
        )