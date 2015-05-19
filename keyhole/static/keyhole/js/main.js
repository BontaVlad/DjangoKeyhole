(function($) {
    function init_editor(e) {
        var editor = $(e);
        var selector = editor.data('selector');
        editor.cropit({
            imageState: {
                src: editor.data('original-image')
            }
        });

        $("body").on('click', '#' + selector + '_btn', function(e) {
            e.preventDefault();
            e.stopPropagation();
          // Move cropped image data to hidden input
          var imageData = editor.cropit('export');
          $('#' + selector).val(imageData);
          return false;
        });
    }

    $(document).ready(function() {
        var editors = $('.image-editor');
        $.each(editors, function(index, value) {
            init_editor(value);
        });
    });

})(django.jQuery);

