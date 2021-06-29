function pygmentize(){

    var filename = $('input[name=filename]').val()

    $.ajax({
        // type: 'post',
        url: "../main.py",
        context: document.body,
        data:{ img_path: filename }
    }).done(function() {
     alert(filename);
     console.log('!!!!!!!!!!!!!!!!!!!!!!!');
    });
}
