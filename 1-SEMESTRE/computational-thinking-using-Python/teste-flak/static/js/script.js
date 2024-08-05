document.addEventListener("DOMContentLoaded", function() {
    //conteúdo que será compartilhado: Título da página + URL
    var conteudo = encodeURIComponent(document.title + " " + window.location.href);
    //altera a URL do botão
    document.getElementById("whatsapp-share-btt").href = "https://api.whatsapp.com/send?text=" + conteudo;
}, false);

document.querySelector('body').addEventListener('mousemove',eyeball);

function eyeball()
{
    var eye = document.querySelectorAll('.eye');
    eye.forEach(function(eye)
    {
        let x = (eye.getBoundingClientRect().left) + (eye.clientWidth / 2);
        let y = (eye.getBoundingClientRect().top) + (eye.clientHeight / 2);


        let radian = Math.atan2(event.pageX - x, event.pageY - y);

        let rot = (radian * (180 / Math.PI) * -1) + 270;

        eye.style.transform = "rotate("+ rot +"deg)";
    })
}