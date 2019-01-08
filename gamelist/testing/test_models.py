from django.test import TestCase

from gamelist.models import GameList, Member
from django.contrib.auth.models import User

# my tests start here
class GameListTestCase(TestCase):
    def setUp(self):
        self.user   = User.objects.create_user(username="testuser", password="testpassword")
        self.member = Member.objects.create(user=self.user)

        GameList.objects.create(
            name = "My best games ever",
            description  = "This is test description",
            views =15,
            owner =self.member
        )

    def test_create_gamelist(self):
        game_list = GameList.objects.get(name="My best games ever")
        self.assertEqual(game_list.name, "My best games ever")
        self.assertEqual(game_list.description, "This is test description")
        self.assertEqual(game_list.views, 15)
        self.assertEqual(game_list.owner, self.member)

    def test__str__(self):
        game_list = GameList.objects.get(name="My best games ever")
        self.assertEqual(game_list.__str__(), "My best games ever")

    def test_slug(self):
        game_list = GameList.objects.get(name="My best games ever")
        self.assertEqual(game_list.slug(), "my-best-games-ever")
        
        
        