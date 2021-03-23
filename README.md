Installation:

* Install `django-mp-attributes`

* Add `'attributes.settings.default'` to settings factory.

* Add `'attributes',` to admin fields.

* Form field:
```
from attributes.fields import AttributesFormField

class Form(...):

    attributes = AttributesFormField(label='')

    def __init__(self, *args, **kwargs):

        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['attributes'].init_form(*args, **kwargs)

    def commit(self, product):

        self.fields['attributes'].commit(product)
```
