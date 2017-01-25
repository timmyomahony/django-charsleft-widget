from django import forms
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


class MediaMixin(object):
    pass

    class Media:
        css = {'screen': ('charsleft-widget/css/charsleft.css',), }
        js = ('charsleft-widget/js/charsleft.js',)


class CharsLeftInput(forms.TextInput):
    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            final_attrs['value'] = force_str(self._format_value(value))
        maxlength = final_attrs.get('maxlength', False)
        if not maxlength:
            return mark_safe(u'<input%s />' % flatatt(final_attrs))
        current = force_str(int(maxlength) - len(value))
        char_remain_str = _(u'characters remaining')
        html = u"""
            <span class="charsleft charsleft-input">
            <input %(attrs)s />
            <span>
                <span class="count">%(current)s</span>
                %(char_remain_str)s</span>
            <span class="maxlength">%(maxlength)s</span>
            </span>
        """ % {
            'attrs': flatatt(final_attrs),
            'current': current,
            'char_remain_str': char_remain_str,
            'maxlength': int(maxlength),
        }
        return mark_safe(html)
