![Screenshot](https://github.com/pastylegs/django-charsleft-widget/raw/master/charsleft-screen-small.jpg)


A simple django widget that appends a character count to a text input which is determined by the `max_length` of that particular field. This only works on __text inputs__ and not __text areas__ (as they don't respect `max_length` anyway)


### Usage ###

There are a few ways of setting a widget for a form field

##### via forms.py #####

	from django import forms
	from charsleft_widget.widgets import CharsLeftInput
	
	class OhGreatLeader(forms.Form):
		name = forms.CharField(widget=CharsLeftInput())

or

	from django import forms
	from charsleft_widget.widgets import CharsLeftInput
	
	class OhGreatLeader(forms.Form):
		name = forms.CharField()

		def __init__(self, *args, *kwargs):
			super(OhGreatLeader, self).__init__(*args, **kwargs)
			self.fields['name'].widget = CharsLeftInput

##### via admin.py #####

	from django.contrib import admin
	class OhGreatLeaderAdmin(admin.ModelAdmin):
		# Use widget on all instances of this form field
		formfield_overrides = {
        	models.TextField: {'widget': CharsLeftInput},
    	}



or

	from django.contrib import admin
	class OhGreatLeaderAdmin(admin.ModelAdmin):
		pass

	# Use widget on particular instances of the form field
	def formfield_for_dbfield(self, db_field, **kwargs):
		if db_field.name is 'name':
			kwargs['widget'] = CharsLeftInput
		return super(ContentObjectAdmin,self).formfield_for_dbfield(db_field,**kwargs)


##### via a custom model field #####

	class CustomModelField(models.CharField):
		pass

    def formfield(self, **kwargs):
        defaults = { 'widget' : CharsLeftInput }
        kwargs.update(defaults)
        return super(CustomModelField, self).formfield(**kwargs)
