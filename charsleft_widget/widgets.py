from django import forms, VERSION
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

try:
    # py2.x
    from django.utils.encoding import force_unicode as force_str
except ImportError:
    # py3.x
    from django.utils.encoding import force_text as force_str
try:
    # Django >=1.7
    from django.forms.utils import flatatt
except ImportError:
    # Django <1.7
    from django.forms.util import flatatt

from charsleft_widget.utils import compatible_staticpath


class CharsLeftInput(forms.TextInput): 

    class Media:
        css={
            "all": ("charsleft-widget/css/charsleft.css", )
        }
        js=(compatible_staticpath("charsleft-widget/js/charsleft.js"), )

    def render(self, name, value, attrs=None, **kwargs):
        if value is None:
            value = ''

        extra_attrs = {
            'type': self.input_type,
            'name': name,
            'maxlength': self.attrs.get('maxlength')
        }
        
        # Signature for build_attrs changed in 1.11
        # https://code.djangoproject.com/ticket/28095
        if VERSION < (1, 11):
            final_attrs = self.build_attrs(attrs, **extra_attrs)
        else:
            final_attrs = self.build_attrs(attrs, extra_attrs=extra_attrs)

        if value != '':
            final_attrs['value'] = force_str(self._format_value(value))

        maxlength = final_attrs.get('maxlength', False)
        if not maxlength:
            return mark_safe(u'<input%s />' % flatatt(final_attrs))

        current = force_str(int(maxlength) - len(value))
        html = u"""
            <span class="charsleft charsleft-input">
            <input %(attrs)s />
            <span>
                <span class="count">%(current)s</span> %(char_remain_str)s</span>
                <span class="maxlength">%(maxlength)s</span>
            </span>
        """ % {
            'attrs': flatatt(final_attrs),
            'current': current,
            'char_remain_str': _(u'characters remaining'),
            'maxlength': int(maxlength),
        }
        return mark_safe(html)
