from django import forms

from game.models import Game

# forms starts here
class GameCreationForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title','game_developer','url','image_cover','description']

    def __init__(self, *args, **kwargs):
        super(GameCreationForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget = forms.TextInput(attrs= {
            'class':'form-control',
            'placeholder':'Game title'
        })

        self.fields['game_developer'].widget = forms.TextInput(attrs= {
            'class':'form-control',
            'placeholder':'Game developer'
        })

        self.fields['url'].widget = forms.TextInput(attrs= {
            'class':'form-control',
            'placeholder':'Enter url'
        })

        self.fields['image_cover'].widget = forms.FileInput(attrs= {
            'class':'form-control',
        })

        self.fields['description'].widget = forms.Textarea(attrs= {
            'class':'form-control',
        })
    