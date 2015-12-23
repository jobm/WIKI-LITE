from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import *
from crispy_forms.layout import (Layout,Field, Fieldset,Reset, Row,
                                 Column, ButtonHolder, Submit)
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)
from django.utils.translation import ugettext as _
from Wiki.models import Article, Draft


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        exclude = ('date_created','date_updated','created','views','slug')
    def __init__(self, *args, **kwargs):
        # Init layout form with crispy
        self.helper = FormHelper()
        self.helper.form_action ='/'
        self.helper.form_method = 'POST'
        self.helper.form_show_labels = True
        self.helper.layout = Layout(
            Field('title'),
            Field('post'),
            Field('category'),
            FormActions(Submit('submit', _('add'),css_class='btn btn-primary btn-lg'),
                        Reset('reset',_('cancel'),css_class='btn btn-danger btn-lg')),
        )
        super(ArticleForm, self).__init__(*args, **kwargs)