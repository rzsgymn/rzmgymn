var script= document.createElement('script');
script.type='text/javascript';
script.src="https://cdn.tiny.cloud/1/829djhntd24le2eg1v9kmy1yce0xqcer8wibohg2o3r8i5vb/tinymce/6/tinymce.min.js";

script.referrerpolicy="origin"

document.head.appendChild(script);

script.onload=function(){
    console.log(123456789)

 tinymce.init({
    selector: "textarea",
    height:656,
    plugins: [
        'advlist autolink link image lists charmap print preview hr anchor pagebreak',
        'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
        'table emoticons template paste help'
      ],
      toolbar: 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | ' +
        'bullist numlist outdent indent | link image | print preview media fullpage | ' +
        'forecolor backcolor emoticons | help code',
      menu: {
        favs: {title: 'My Favorites', items: 'code visualaid | searchreplace | emoticons'}
      },
      menubar: 'favs file edit view insert format tools table help',
      content_css: 'css/content.css'
    });
}

