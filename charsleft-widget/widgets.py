from django import forms
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.utils.html import escape, conditional_escape
from django.forms.util import flatatt

class MediaMixin(object):
	pass
	
	class Media:
		css = {'screen':('charsleft-widget/css/charsleft.css',),}
		js = ('charsleft-widget/js/charsleft.js',)
	
class CharsLeftInput(forms.TextInput, MediaMixin): 
			
	def render(self, name, value, attrs=None):
		if value is None:
			value = ''
		final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
		if value != '':
			final_attrs['value'] = force_unicode(self._format_value(value))
		maxlength = final_attrs.get('maxlength',False)
		if not maxlength:
			return mark_safe(u'<input%s />'%flatatt(final_attrs))
		current = force_unicode(int(maxlength) - len(value))
		html = u"""
			<span class="charsleft charsleft-input">
			<input %(attrs)s /> 
			<span><span class="count">%(current)s</span> characters remaining</span>
			<span class="maxlength">%(maxlength)s</span>
			</span>
		""" % { 
			'attrs':flatatt(final_attrs),
			'current':current,
			'maxlength':int(maxlength),
		}
		return mark_safe(html)