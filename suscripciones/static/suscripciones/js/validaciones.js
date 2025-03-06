/*COOCKIE PARA GUARDAR EL TOKEN*/
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



/*FORMULARIO DE REGISTRO CON JS*/
if (document.body.classList.contains('')) {
    var usuario = document.getElementsByName('username')[0];
    var contrasenna = document.getElementsByName('password')[0];
    var correo = document.getElementsByName('email')[0];




    function JsRegistrar() {
        var okay = true;
        var usuarioValue = usuario.value.trim();
        var correoValue = correo.value.trim();
        var contrasennaValue = contrasenna.value.trim();

        if (usuarioValue === '') {
            setErrorFor(usuario, 'No puede dejar el usuario en blanco.')
            okay = false;

        } else {
            setSuccessFor(usuario);
        }
        if (correoValue === '') {
            setErrorFor(correo, 'No puede dejar el correo electrónico en blanco');
            okay = false;
        } else if (!isEmail(correoValue)) {
            setErrorFor(correo, 'No ingreso un correo electrónico válido');
            okay = false;
        } else {
            setSuccessFor(correo);
        }

        if (contrasennaValue === '') {
            setErrorFor(contrasenna, 'No debe dejar en blanco la contraseña');
            okay = false;
        } else {
            setSuccessFor(contrasenna);
        }
        return okay;
    }

    function setSuccessFor(input) {
        var formControl = input.parentElement;
        formControl.className = 'formu-control success';
    }


    function setErrorFor(input, message) {
        var formControl = input.parentElement;
        var small = formControl.querySelector('small');
        formControl.className = 'formu-control error';
        small.innerText = message;
    }


}



/*FORMULARIO DE CONTACTO CON JS  */
if (document.body.classList.contains('formulariocontacto')) {
    var usuario = document.getElementById('user1');
    var telefono = document.getElementById('telefono');
    var correo = document.getElementById('correo');
    var mensaje = document.getElementById('mensaje');

    form.addEventListener('submit', e => {
        e.preventDefault();

        JsContacto();
    });

    function JsContacto() {
        var usuarioValue = usuario.value.trim();
        var telefonoValue = telefono.value.trim();
        var correoValue = correo.value.trim();
        var mensajeValue = mensaje.value.trim();


        if (usuarioValue === '') {
            setErrorFor(usuario, 'No puede dejar el Nombre en blanco.')

        } else {
            setSuccessFor(usuario);
        }

        if (telefonoValue === '') {
            setErrorFor(telefono, 'No puede dejar el telefono en blanco.')

        } else {
            setSuccessFor(telefono);
        }

        if (correoValue === '') {
            setErrorFor(correo, 'No puede dejar el correo  en blanco');
        } else if (!isEmail(correoValue)) {
            setErrorFor(correo, 'No ingreso un correo  válido');
        } else {
            setSuccessFor(correo);
        }

        if (mensajeValue === '') {
            setErrorFor(mensaje, 'No puede dejar el mensaje en blanco.')

        } else {
            setSuccessFor(mensaje);
        }
    }

    function setSuccessFor(input) {
        var formControl = input.parentElement;
        formControl.className = 'form-groupoo success';
    }


    function setErrorFor(input, message) {
        var formControl = input.parentElement;
        var small = formControl.querySelector('small');
        formControl.className = 'form-groupoo error';
        small.innerText = message;
    }


}




/*FORMULARIO INICIO SESIÓN CON JQ */


$(document).ready(function() {
    $("#JEnviar").click(function() {
        var nombre = $("#users").val();
        var contrasenna = $("#pass").val();

        if (nombre == "") {
            $("#mensaje1").show();


        } else {
            $("#mensaje1").hide();

        }
        if (contrasenna == "") {
            $("#mensaje2").show();


        } else {
            $("#mensaje2").hide();

        }

    });



});
/* API EXTERNA*/
$.get("static/suscripciones/api/models.json", function(data) {
    $.each(data.mecanicos, (function(i, mecanico) {
        let nombre = document.createElement("h5");
        nombre.innerHTML = 'Nombre: ' + mecanico.nombre;

        let edad = document.createElement("h5");
        edad.innerHTML = 'Edad: ' + mecanico.edad;

        let telefono = document.createElement("h5");
        telefono.innerHTML = 'Telefono: ' + mecanico.telefono;

        let caption = document.createElement("div");
        caption.className = 'carousel-caption d-none d-lg-block';
        caption.appendChild(nombre);
        caption.appendChild(edad);
        caption.appendChild(telefono);

        let img = document.createElement("img");
        img.setAttribute('src', mecanico.imagen);
        img.setAttribute('alt', mecanico.nombre);
        img.setAttribute('style', 'width: 50%; margin-left: 50%;');

        carousel = document.createElement("div");
        carousel.appendChild(img);
        carousel.appendChild(caption);
        if (i === 0) {
            carousel.className = 'carousel-item active';
        } else {
            carousel.className = 'carousel-item';
        }
        $("#carrusel").append(carousel);

    }));
});







/* VALIDADOR DE TOKEN REGISTRO*/
if (document.body.classList.contains('registro')) {

    $('#form-registro').on('submit', function(e) {
        $.ajax({
            url: '/knox/valida-form-registro/',
            type: 'POST',
            dataType: "json",
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
            },
            data: $(this).serialize(),
            success: function(response) {
                if (JSON.stringify(response).includes('url')) {
                    window.location = JSON.parse(JSON.stringify(response.url));
                } else {
                    $('#error-registro').html(JSON.parse(JSON.stringify(response['mensaje'])));
                }
            },
        });
        e.preventDefault();
    });
}

/* VALIDADOR DE TOKEN LOGIN*/
if (document.body.classList.contains('login1')) {

    $('#form-login').on('submit', function(e) {
        $.ajax({
            url: '/knox/valida-form/',
            type: 'POST',
            dataType: "json",
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
            },
            data: $(this).serialize(),
            success: function(response) {
                if (JSON.stringify(response).includes('url')) {
                    window.location = JSON.parse(JSON.stringify(response.url));
                } else {
                    $('#error-login').html(JSON.parse(JSON.stringify(response['mensaje'])));
                }
            },
        });
        e.preventDefault();
    });
}






const token = getCookie('sessiontoken')
const csrftoken = getCookie('csrftoken');

$(document).ready(function() {
    BindServicios();
});
/* POST*/
$('#btnSubmit').click(function() {


    let nombreservicio = $('#txtservicio').val();
    let precio = $('#txtprecio').val();
    $.ajax({

        type: 'POST',
        dataType: 'json',
        headers: { 'Authorization': 'Token ' + token, 'X-CSRFToken': csrftoken },

        data: {
            "nombreservicio": nombreservicio,
            "precio": precio
        },

        url: "/API/lista_servicio",
        error: function(xhr, status, error) {

            var err_msg = ''
            for (var prop in xhr.responseJSON) {
                err_msg += prop + ': ' + xhr.responseJSON[prop] + '\n';
            }

            alert(err_msg);
        },
        success: function(result) {

            BindServicios();


            $('#txtId').val("");
            $('#txtservicio').val("");
            $('#txtprecio').val("");

        }
    });
});
/* GET*/
function BindServicios() {
    $.ajax({
        type: 'GET',
        dataType: 'json',
        headers: { 'Authorization': 'Token ' + token, 'X-CSRFToken': csrftoken },

        url: "/API/lista_servicio",
        success: function(result) {

            var totalCount = result.length;
            var structureDiv = "";
            for (let i = 0; i < totalCount; i++) {
                structureDiv += "<tr>" +
                    "     <td>" + result[i].idservicio + "</td>" +
                    "      <td>" + result[i].nombreservicio + "</td>" +
                    "             <td>" + result[i].precio + "</td>" +
                    "              <td><button class='btn btn-light' onclick='return confirm(\"Está seguro de que desea eliminar este servicio?\",DeleteRow(" + result[i].idservicio + "))'>Eliminar</button></td>" +
                    "           </tr>";
            }

            $("#divBody").html(structureDiv);

        }
    });

}
/*function PutRow(id) {

    $.ajax({
        type: 'PUT',
        dataType: 'json',
        headers: { 'Authorization': 'Token ' + token, 'X-CSRFToken': csrftoken },
        url: "/API/detalle_servicio/" + id,
        data: {
            "nombreservicio": nombreservicio,
            "precio": precio
        },
        success: function(result) {

            BindServicios();
        }
    });
}



/* DELETE*/
function DeleteRow(id) {

    $.ajax({
        type: 'DELETE',
        dataType: 'json',
        headers: { 'Authorization': 'Token ' + token, 'X-CSRFToken': csrftoken },
        url: "/API/detalle_servicio/" + id,
        error: function(xhr, status, error) {

            var err_msg = ''
            for (var prop in xhr.responseJSON) {
                err_msg += prop + ': ' + xhr.responseJSON[prop] + '\n';
            }

            alert(err_msg);
        },
        success: function(result) {

            BindServicios();
        }
    });
}