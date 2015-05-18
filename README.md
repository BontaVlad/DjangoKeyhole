# DjangoKeyhole

DjangoKeyhole is a Django addon that adds an image crop widget to the standard ImageField. The actual cropping is done by the wonderful jquery cropping library [cropit](http://scottcheng.github.io/cropit/)

  - quick and easy instalation
  - no external dependencyes
  - magic.


### Installation

```sh
$ pip install DjangoKeyhole
```
Add ```keyhole``` to you're ```INSTALLED_APPS``` in ```settings.py```

Last but not least
```sh
$ python manage.py collectstatic
```

### How to use

```python
from django.contrib import admin

#import the widget
from keyhole.widgets import CroppedImageWidget

class MyAdminForm(forms.ModelForm):
    # width and height are in px
    foo_image = forms.ImageField(widget=CroppedImageWidget(width=160, height=160))
```

### Todo's

 - Write Tests
 - Fix typos in text
 - Add Code Comments
 - Test in pyhon 2.7

### Version
0.1

License
----
MIT

**Free Software, Hell Yeah!**
