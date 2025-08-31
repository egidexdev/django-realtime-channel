from django import forms
from .models import GroupMessage

class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={
                'placeholder': 'Add message ...',
                'class': 'p-4 text-black w-full rounded-xl border border-gray-600',
                'maxlength': '300',
                'autofocus': True
            }),
        }
