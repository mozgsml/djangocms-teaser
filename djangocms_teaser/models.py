from cms.models import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField
from django.db import models
from django.conf import settings
from django.utils.text import Truncator
from django.utils.html import strip_tags
from django.utils.translation import ugettext, ugettext_lazy as _



# Add additional choices through the ``settings.py``.
def get_templates():
    choices = [
        ('default', _('Default')),
    ]
    choices += getattr(
        settings,
        'DJANGOCMS_TEASER_TEMPLATES',
        [],
    )
    return choices

def get_default_template():
    return getattr(
        settings,
        'DJANGOCMS_TEASER_DEFAULT_TEMPLATE',
        get_templates()[0][0],
    )

class Tiser(CMSPlugin):
    image = FilerImageField(
        null=True,
        blank=True,
        default=None,
        verbose_name=_('Image'),
        on_delete=models.SET_NULL,
    )
    header = models.CharField(_('Header'), max_length=128, null=True, blank=True)
    text = HTMLField(_('Text'), null=True, blank=True)

    template = models.CharField(
        verbose_name=_('Template'),
        choices=get_templates(),
        default=get_default_template,
        max_length=255,
    )

    def get_title(self):
        return self.header

    def __str__(self):
        return self.get_title()
