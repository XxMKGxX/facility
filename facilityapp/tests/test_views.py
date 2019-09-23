import urllib
import datetime
from django.test import TestCase, Client
from django.contrib.auth.models import User
from facilityapp.models import *

class FacilityViewTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client

    @classmethod
    def setUpTestData(cls):
        cls.facility = Facility.objects.create(facility_name='test', length='1', width='1', height='1', floor_area='2', site_area='3')
        cls.usr = User.objects.create_user(username='someone')

    def test_get_facility_list(self):
        resp = self.client.get('/facilities/facility-list')
        self.assertEqual(resp.status_code, 200)

    def test_get_facility_detail(self):
        resp = self.client.get('/facilities/facility-detail/'+str(self.facility.pk))
        self.assertEqual(resp.status_code, 200)

    def test_get_facility_update(self):
        resp = self.client.get('/facilities/facility-update/'+str(self.facility.pk))
        self.assertEqual(resp.status_code, 200)

    def test_get_facility_create(self):
        resp = self.client.get('/facilities/facility-create/')
        self.assertEqual(resp.status_code, 200)


