from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['comment']

    def clean_comment(self):
        comment = self.cleaned_data['comment']

        if len(comment) < 10:
            raise forms.ValidationError(
                "Review must be at least 10 characters long."
            )

        return comment