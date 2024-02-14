from django import forms
from .models import SeekingAd

class CommentForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": "6",
                "cols": "20",
                "class": "form-control"
            }
        )
    )
class SeekingAdForm(forms.ModelForm):
    class Meta:
        model = SeekingAd
        fields = ["seeking", "musician", "band", "content", ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["seeking"].widget.attrs.update({'class': 'form-control'})
        self.fields["musician"].widget.attrs.update({'class': 'form-control'})
        self.fields["band"].widget.attrs.update({'class': 'form-control'})
        self.fields["content"].widget.attrs.update({'class': 'form-control'})
