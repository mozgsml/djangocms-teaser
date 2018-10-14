from cms.models import CMSPlugin
from cms.models.fields import PageField
from djangocms_attributes_field.fields import AttributesField
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField
from django.db import models
from django.conf import settings
from django.utils.text import Truncator
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _

LINK_TARGET = (
    ('_blank', _('Open in new window')),
    ('_self', _('Open in same window')),
    ('_parent', _('Delegate to parent')),
    ('_top', _('Delegate to top')),
)


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
        default=get_default_template(),
        max_length=255,
    )

    # link models
    link_url = models.URLField(
        verbose_name=_('External URL'),
        blank=True,
        max_length=2040,
        help_text=_('Wraps the image in a link to an external URL.'),
    )
    link_page = PageField(
        verbose_name=_('Internal URL'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text=_('Wraps the image in a link to an internal (page) URL.'),
    )
    link_target = models.CharField(
        verbose_name=_('Link target'),
        choices=LINK_TARGET,
        blank=True,
        max_length=255,
    )
    link_attributes = AttributesField(
        verbose_name=_('Link attributes'),
        blank=True,
        excluded_keys=['href', 'target'],
    )

    def get_title(self):
        if (self.header is None):
            return Truncator(strip_tags(self.text).replace('&shy;', '')).words(3, truncate="...")
        else:
            return self.header

    def __str__(self):
        return self.get_title()

    def get_link(self):
        if self.link_url:
            return self.link_url
        if self.link_page_id:
            return self.link_page.get_absolute_url(language=self.language)
        return False
