import sys
import re
import base64
try:
    from io import BytesIO
except ImportError:
    from cStringIO import StringIO as BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.safestring import mark_safe
from django import forms


class CroppedImageWidget(forms.widgets.FileInput):

    class Media:
        css = {
            'all': ('keyhole/css/style.css', )
        }
        js = ('keyhole/js/jquery.cropit.js',
              'keyhole/js/main.js')

    def __init__(self, height, width, attrs=None):
        super(CroppedImageWidget, self).__init__(attrs)
        self.height = height
        self.width = width

    def _get_image_data(self, encoded_data):
        splitted = encoded_data.split(',')
        pattern = re.compile(':(\w+/\w+);')

        m = pattern.findall(splitted[0]) if splitted else []
        content_type = m[0] if m else None
        image_bytes = splitted[1] if splitted else None

        return content_type, image_bytes

    def _get_url(self, value, default=''):
        # must be a better way to handle all the cases
        if not value:
            return default
        try:
            # could be ImMemoryFile, so we check for url dynamically
            image_url = getattr(value, 'url', '')
        except ValueError:
            # this means that ImageField is empty usually because it is
            # blank=True in the model
            pass
        return image_url or default

    def render(self, name, value, attrs=None):
        html = """
        <div class="image-editor" data-original-image="{image_url}"
             data-selector="id_{field_name}">
            <input type="file" class="cropit-image-input">
            <div class="cropit-image-preview"
                style="width:{width}px;height:{height}px;"></div>
            <ul class="slider-wrapper">
                <li><span class="icon icon-small"></span></li>
                <li><input type="range" class="cropit-image-zoom-input"></li>
                <li><span class="icon icon-large"></span></li>
            </ul>
            <input type="hidden" name="{field_name}" id="id_{field_name}"
                class="hidden-image-data" />
        </div>
        """.format(
            image_url=self._get_url(value), height=self.height,
            width=self.width, field_name=name)
        return mark_safe(html)

    def value_from_datadict(self, data, files, name):
        encoded_data = data.get(name, None)
        bytestream = None

        if encoded_data:
            content_type, image_bytes = self._get_image_data(encoded_data)
            if all([content_type, image_bytes]):
                bytestream = BytesIO(base64.b64decode(image_bytes))
                if bytestream:
                    image = InMemoryUploadedFile(
                        bytestream, field_name='file', name='photo',
                        content_type=content_type,
                        size=sys.getsizeof(bytestream),
                        charset=None)
                    return image
        return encoded_data
