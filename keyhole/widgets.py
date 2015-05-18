import sys
import re
import base64
try:
    from io import BytesIO
except ImportError:
    from cStringIO import StringIO as BytesIO

from django.utils.translation import ugettext as _
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.safestring import mark_safe
from django import forms


class CroppedImageWidget(forms.widgets.FileInput):

    class Media:
        css = {
            'all': ('crop_widget/css/style.css', )
        }
        js = ('crop_widget/js/jquery.cropit.js',
              'crop_widget/js/main.js')

    def __init__(self, height, width, attrs=None):
        super().__init__(attrs)
        self.height = height
        self.width = width

    def render(self, name, value, attrs=None):
        # ugly but effective
        html = """
        <div class="image-editor" data-original-image="{image_url}"
             data-field-id="id_{field_name}">
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
        <a href="#" class="grp-button crop">{button_label}</a>
        """.format(
            image_url=value.url, height=self.height, width=self.width,
            field_name=name, button_label=_('Set croped image'))
        return mark_safe(html)

    def value_from_datadict(self, data, files, name):
        initial = data.get(name, None)
        if initial:
            base64_splitted = initial.split(',')
            pattern = re.compile(':(\w+/\w+);')
            content_type = pattern.findall(base64_splitted[0])[:1]
            base64_stripped = base64_splitted[1]
        if base64_stripped:
            image_file = BytesIO(base64.b64decode(base64_stripped))
        if image_file:
            image = InMemoryUploadedFile(
                image_file, field_name='file', name='photo',
                content_type=content_type, size=sys.getsizeof(image_file),
                charset=None)
            return image
        return initial
