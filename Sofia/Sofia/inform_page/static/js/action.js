$( document ).ready(function() {
    var quill = new Quill('#editor', {
        theme: 'snow',
        modules: {
            toolbar: [
              [{ header: [1, 2, false] }],
              ['bold', 'italic', 'underline'],
              ['image', 'code-block']
            ]
          },
      });
});

