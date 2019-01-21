from django import forms

from community.models import Posts, Forum
from game.models import Game

class PostCreationForm(forms.ModelForm):
    
    class Meta:      
        model = Posts
        fields = ['post',]

    def __init__(self, *args, **kwargs):
        super(PostCreationForm, self).__init__(*args, **kwargs)

        self.fields['post'].widget = forms.Textarea(attrs={
            'class':'form-control',
            'id':'forumTextArea',
            'placeholder':'Add your contribution to the group',
            'cols':30,
        })
    
    
class ForumCreationForm(forms.ModelForm):

    class Meta:
        model = Forum
        fields = ['topic',]

    def __init__(self, *args, **kwargs):
        super(ForumCreationForm, self).__init__(*args, **kwargs)

        self.fields['topic'].widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Enter topic for your forum',
        })