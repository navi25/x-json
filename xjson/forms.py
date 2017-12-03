from django import forms

from xjson.models import Document


#class DocumentForm(forms.ModelForm):
#    class Meta:
#        model = Document
#        fields = ('description', 'document', )


class NewDocForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput)

""" def clean(self):
        cleaned_data = super(NewDocForm,self).clean()
        file = self.cleaned_data.get('file')
        newq = self.cleaned_data.get('newq')

        return cleaned_data
        if not file:
            raise forms.ValidationError('Fields Needed')
"""

