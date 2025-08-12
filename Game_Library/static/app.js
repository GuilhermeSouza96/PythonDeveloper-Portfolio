$('form input[type="file"]').change(event => {
    let archives = event.target.files;
    if (archives.length === 0) {
        console.log('No image to display')
    } else {
        if (archives[0].type == 'image/jpeg') {
            $('img').remove();
            let image = $('<img class="img-responsive">');
            image.attr('src', window.URL.createObjectURL(archives[0]));
            $('figure').prepend(image)
        } else {
            alert('Format not supported')
        }
    }
});