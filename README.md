![Screenshot](https://github.com/timmyomahony/django-charsleft-widget/blob/master/charsleft-screen-small.jpg?raw=true)


A simple django widget that appends a character count to a text input which is determined by the `max_length` of that particular field. This only works on __text inputs__ and not __text areas__ (as they don't respect `max_length` anyway)


### Usage ###

There are a few ways of setting a widget for a form field

##### via forms.py #####

	from django import forms
	from charsleft_widget.widgets import CharsLeftInput
	
	class ExampleForm(forms.Form):
		name = forms.CharField(widget=CharsLeftInput())

or

	from django import forms
	from charsleft_widget.widgets import CharsLeftInput
	
	class ExampleForm(forms.Form):
		name = forms.CharField()

		def __init__(self, *args, *kwargs):
			super(ExampleForm, self).__init__(*args, **kwargs)
			self.fields['name'].widget = CharsLeftInput

##### via admin.py #####

	from django.contrib import admin
	class ExampleAdmin(admin.ModelAdmin):
		# Use widget on all instances of this form field
		formfield_overrides = {
        	models.TextField: {'widget': CharsLeftInput},
    	}



or

	from django.contrib import admin
	class ExampleAdmin(admin.ModelAdmin):
		pass

	# Use widget on particular instances of the form field
	def formfield_for_dbfield(self, db_field, **kwargs):
		if db_field.name is 'name':
			kwargs['widget'] = CharsLeftInput
		return super(ContentObjectAdmin,self).formfield_for_dbfield(db_field,**kwargs)
