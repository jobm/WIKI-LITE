from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field ,Reset, Submit, Button
from crispy_forms.bootstrap import FormActions
from django.utils.translation import ugettext as _
from Wiki.models import Article, Draft


class ArticleAddForm(ModelForm):

    class Meta:
        model = Article
        exclude = ('date_created','date_updated','created','views','slug')

    def __init__(self, *args, **kwargs):
        super(ArticleAddForm, self).__init__(*args, **kwargs)
        # Init layout form with crispy
        self.helper = FormHelper()
        self.helper.form_action ='/wiki/add/'
        self.helper.form_method = 'POST'
        self.helper.form_show_labels = True
        self.helper.layout = Layout(

            Field('title'),
            Field('post'),
            Field('category'),

            FormActions(
                Submit('submit', _('add'), css_class='btn btn-primary btn-lg'),
                Reset('reset', _('cancel'), css_class='btn btn-danger btn-lg')
            ),
        )


class ArticleEditForm(ModelForm):

    class Meta:
        model = Article
        exclude = ('date_created','date_updated','created','views','slug')

    def __init__(self, *args, **kwargs):
        super(ArticleEditForm, self).__init__(*args, **kwargs)
        # Init layout form with crispy
        self.helper = FormHelper()
        self.helper.form_action ='/wiki/update/'
        self.helper.form_method = 'POST'
        self.helper.form_show_labels = True
        self.helper.layout = Layout(
            Field('title'),
            Field('post'),
            Field('category'),
            FormActions
                (
                    Submit('submit', _('update'), css_class='btn btn-primary btn-lg'),
                    Reset('reset', _('cancel'), css_class='btn btn-warning btn-lg'),
                ),

        )