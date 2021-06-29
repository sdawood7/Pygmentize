function pygmentize(the_name_of_the_file){
    $.ajax({
        url: "../test.py",
        context: document.body,
        data:{}
    }).done(function() {
     alert('pygmentized!!');
     console.log('!!!!!!!!!!!!!!!!!!!!!!!');
    });
}
