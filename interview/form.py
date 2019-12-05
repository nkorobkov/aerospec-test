from django import forms
from interview.models import Panel, Site


class IssueForm(forms.Form):
    panel = forms.ModelChoiceField(Panel.objects.using('interview_db').all(), label='panel')
    site = forms.ModelChoiceField(Site.objects.using('interview_db').all(), label='site')
    comment = forms.CharField(label='comment', max_length=1024, widget=forms.Textarea(), required=False)
