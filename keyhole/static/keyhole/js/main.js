(function($) {
    $(function() {
        var editor = $('.image-editor');
        var field_id = editor.data('field-id');
        editor.cropit({
            imageState: {
                src: editor.data('original-image')
            }
        });

        $('.crop').click(function(e) {
            e.preventDefault();
            e.stopPropagation();
          // Move cropped image data to hidden input
          var imageData = editor.cropit('export');
          $('#' + field_id).val(imageData);

          return false;
        });
      });
})(django.jQuery);

