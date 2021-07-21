let imageUrl;

function changeUrl(){
    imageUrl = URL.createObjectURL(event.target.files[0]);
}

function submit(){
    let image = document.getElementById('mainImg');
    if (imageUrl)
    {
        image.src = imageUrl;
    }
}