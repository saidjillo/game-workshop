from django import forms

from gamelist.models import GameList

# forms start here
class GameListCretionForm(forms.ModelForm):
    class Meta:
        model  = GameList
        fields =  ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(GameListCretionForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Name'
        })

        self.fields['description'].widget = forms.Textarea(attrs= {
            'class':'form-control',
            'placeholder':'describe game collection'
        })
    
