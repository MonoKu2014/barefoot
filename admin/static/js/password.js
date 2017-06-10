
$(document).ready(function(){

    var femail=$('#form_email');
    var fnormal=$('#form_normal');
    var fcodigo=$("#form_codigo")
    var acodigo=$('#a_codigo');
    var error_recupera=$("#error_recupera");
    var ok_recupera=$("#ok_recupera")

    var error_codigo=$("#error_codigo");
    var ok_codigo=$("#ok_codigo")

    var volver=$(".btn_volver");

    var enviar=$("#btn_recupera");
    var email=$("#email");

    var codigo=$("#codigo");

    $("#a_recupera").click(function(){

        fnormal.slideUp(200,function(){
            acodigo.show();
            fcodigo.hide();
            femail.slideDown(500)

        })


    });


    $("#a_codigo").click(function(){

        femail.slideUp(200,function(){
            acodigo.show();
            femail.hide();
            fcodigo.slideDown(500)
        })

    });

    enviar.click(function(){

       if(email.val().trim()==""){

           email.addClass("error_password")
           alert("campo email de recuperacion no puede estar vacio")
           return;
       }

        $.post( "/reset_password", { email: email.val() },function(data){

               if(data=="ERROR01"){

                   error_recupera.html("El mail no existe para este usuario");
                   error_recupera.css('margin-bottom','15px')
                   error_recupera.show();
                   ok_recupera=hide();
               }else if(data=="SUCCESS"){

                   ok_recupera.html("se ha enviado un codigo de activacion a tu mail");
                   email.attr('disabled','disabled')
                   ok_recupera.css('margin-bottom','15px')
                   error_recupera.hide();
                   ok_recupera.show();
               }




        });


    });

    $("#btn_codigo").click(function() {


        $.post("/check_code", {email: email.val(), codigo: codigo.val()}, function (data) {

            if (data == "ERROR01") {

                error_codigo.html("El codigo es incorrecto");
                error_codigo.css('margin-bottom', '15px')
                error_codigo.show();
                ok_codigo = hide();
            } else if (data == "SUCCESS") {

                ok_codigo.html("utilize como password el codigo que se le envio a su mail , actualizelo su password a la brevedad");
                ok_codigo.css('margin-bottom', '15px')
                error_codigo.hide();
                $("#btn_codigo").hide();
                ok_codigo.show();
            }


        })
    })

    volver.click(function(){

        acodigo.hide();
        reiniciar();
    })


    function reiniciar(){

        femail.hide();
        fcodigo.hide();

        fnormal.slideDown(500)
    }

    $("#btn_recupera").click(function() {


        var email = $("#email")

        if (email.val().trim() == "") {
            email.addClass("error_password")
        }
    })

})
