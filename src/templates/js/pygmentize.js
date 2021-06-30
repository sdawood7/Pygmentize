// function pygmentize(){

//     var filename = $('input[name=filename]').val()

//     $.ajax({
//         // type: 'post',
//         url: "../main.py",
//         context: document.body,
//         data:{ img_path: filename }
//     }).done(function() {
//      alert(filename);
//      console.log('!!!!!!!!!!!!!!!!!!!!!!!');
//     });
// }
function pygmentize(){
    //document.querySelector('#input').value
    //input[type=submit].value;
    //creating a variable and grabbing the info/data from the myFile input
    // let img = document.querySelector('#myFile').value;
    // creating a variable called image that is just the file/img we want to replace
    let image = document.getElementById('mainImg');
    
    image.src = URL.createObjectURL(event.target.files[0]);
    alert('done')
}
