(function($) {
    function init_editor(e) {
        var editor = $(e);
        var selector = editor.data('selector');
        editor.cropit({
            imageState: {
                src: editor.data('original-image')
            }
        });

        $("form[class*='form'").submit(function( event ) {
            // Move cropped image data to hidden input
            var imageData = editor.cropit('export');
            $('#' + selector).val(imageData);
        });
    }

    $(document).ready(function() {
        var editors = $('.image-editor');
        $.each(editors, function(index, value) {
            init_editor(value);
        });
    });

})(django.jQuery);
