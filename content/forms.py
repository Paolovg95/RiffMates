from django import forms

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
