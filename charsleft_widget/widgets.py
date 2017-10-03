from django import forms
from django.utils.safestring import mark_safe

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
        css = {'screen': ('charsleft-widget/css/charsleft.css',)}
        js = ('charsleft-widget/js/charsleft.js',)


class CharsLeftInput(forms.TextInput, MediaMixin): 

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        extra_attrs = {'type': self.input_type, 'name': name,
                       'maxlength': self.attrs.get('maxlength')}
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
            <span><span class="count">%(current)s</span> characters remaining</span>
            <span class="maxlength">%(maxlength)s</span>
            </span>
        """ % {'attrs': flatatt(final_attrs),
               'current': current,
               'maxlength': int(maxlength)}
        return mark_safe(html)
