from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext, ugettext_lazy as _
from .models import *

class TiserPlugin(CMSPluginBase):
    name = _("Teaser")
    render_template = "djangocms_teaser/default.html"
    model = Tiser

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_teaser/{}.html'.format(instance.template)

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

    fieldsets = [
        (None, {
            'fields': (
                'image',
                'header',
                'text',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'template',
            )
        }),
    ]

plugin_pool.register_plugin(TiserPlugin)
