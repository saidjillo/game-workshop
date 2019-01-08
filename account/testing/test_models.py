from django.test import TestCase
from django.contrib.auth.models import User

from account.models import Member

# my tests start here
class MemberTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        Member.objects.create(user=self.user)

    def test_create_member(self):
        member = Member.objects.get(user__username="testuser")
        self.assertEqual(member.user.username,"testuser")

    def test__str__(self):
        member = Member.objects.get(user__username="testuser")
        self.assertEqual(member.__str__(),"testuser")