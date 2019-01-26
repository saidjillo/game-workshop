from django.test import TestCase

from django.contrib.auth.models import User
from gamelist.models import GameList
from account.models import Member
from game.models import Game

# my tests start here
class GameTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.member = Member.objects.create(user=self.user)
        self.game_list =  GameList.objects.create(
            name = "My best games ever",
            description  = "This is test description",
            views =15,
            owner =self.member
        )

        # create game objects
        Game.objects.create(
            title="pacman 2018",
            description="test description",
            game_developer="galana",
            url="https://www.youtube.com/watch?v=mIBEl26er6Y",
            views=20,
            game_list=self.game_list
        )

    # def test_create_game(self):
    #     game = Game.objects.get(title="pacman 2018")
    #     self.assertEqual(game.title, "pacman 2018")
    #     self.assertEqual(game.description, "test description")
    #     self.assertEqual(game.game_developer, "galana")
    #     self.assertEqual(game.url, "https://www.youtube.com/watch?v=mIBEl26er6Y")
    #     self.assertEqual(game.views,20)

    def test__str__(self):
        game = Game.objects.get(title="pacman 2018")
        self.assertEqual(game.__str__(), "pacman 2018")
        self.assertEqual(5,5)
      

        
