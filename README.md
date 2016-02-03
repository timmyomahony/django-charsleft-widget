![Screenshot](https://github.com/timmyomahony/django-charsleft-widget/blob/master/charsleft-screen-small.jpg?raw=true)

A simple django widget that appends a character count to a text input which is determined by the `max_length` of that particular field. This only works on text *inputs* and not *text areas* (as they don't respect `max_length` anyway)

##Installation

The package can be installed via:
      
    pip install git+https://github.com/timmyomahony/django-charsleft-widget.git
  

##Usage

There are a few ways of setting a widget for a form field:

###via forms.py

```python
from django import forms
from charsleft_widget.widgets import CharsLeftInput
  
class ExampleForm(forms.Form):
  name = forms.CharField(widget=CharsLeftInput())
```

or

```python
from django import forms
from charsleft_widget.widgets import CharsLeftInput
  
class ExampleForm(forms.Form):
  name = forms.CharField()

  def __init__(self, *args, *kwargs):
    super(ExampleForm, self).__init__(*args, **kwargs)
    self.fields['name'].widget = CharsLeftInput
```

### via admin.py #####

```python
from django.contrib import admin
from charsleft_widget.widgets import CharsLeftInput, MediaMixin
    
# The MediaMixin is what loads the css and javascript only one time per admin page
class ExampleAdmin(MediaMixin, admin.ModelAdmin):
  # Use widget on all instances of this form field
  formfield_overrides = {
    models.TextField: {'widget': CharsLeftInput()},
  }
```

or

```python
from django.contrib import admin
from charsleft_widget.widgets import CharsLeftInput, MediaMixin
  
# The MediaMixin is what loads the css and javascript only one time per admin page
class MyModelAdmin(MediaMixin, admin.ModelAdmin):
  pass
  
  # Use widget on particular instances of the form field
  def formfield_for_dbfield(self, db_field, **kwargs):
    if db_field.name is 'my_field_name':
      kwargs['widget'] = CharsLeftInput(attrs={'size':'add normal attrs here, like field size numbers'})
    return super(ContentObjectAdmin,self).formfield_for_dbfield(db_field,**kwargs)
```
