var rol=$("#id_roles[name='roles']");
var ing_precio=$("#ing_solar_control");
var ing_solar=$("#id_ing_solar");

$(document).ready(function(){


    id_ing=ing_solar.val()
    rol.change(function(){

       var rol_sel=rol.val();

        if(rol_sel==id_ing){

           ing_precio.show()
        }else{
            ing_precio.hide()
        }

    });

    rol.trigger('change')
});