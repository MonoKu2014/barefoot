$(document).ready(function(){

$("#submit_btn").click(function(){

    $(".form-control").removeAttr('disabled');
    $("form#form_taller_solar").submit();

})

$('#habilitado:checkbox').change(function(){

    if(!this.checked){
        $(".form-control").attr('disabled','disabled');
    }else{
        $(".form-control").removeAttr('disabled')

    }
});

    $("#habilitado:checkbox").trigger('change')


});
