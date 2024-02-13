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
        labels = {
            "seeking": 'I am seeking a'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["seeking"].label = self.labels["seeking"]
        self.fields["musician"].help_text = \
            "Fill in if you are a musician seeking a band"
        self.fields["band"].help_text = \
            "Fill in if you are a band seeking a musician"
