
var area_id = $('#area').val();
if(area_id !== undefined){
	cargar_seccion(area_id);
}



$(document).on('change', '#area, #area_edit', function(){
    area_id = $(this).val();
    cargar_seccion(area_id);
});


$(document).on('change', '#seccion, #seccion_edit', function(){
    seccion_id = $(this).val();
    cargar_proceso(seccion_id);    
});





function cargar_seccion(area_id)
{
    $.ajax({
      type: 'get',
      url: APP_URL + '/ajax/procesos/secciones_por_area/' + area_id,
      success: function(result){
        $('#seccion').empty().html(result);
      }
    });  
}



function cargar_proceso(seccion_id)
{
    $.ajax({
      type: 'get',
      url: APP_URL + '/ajax/procesos/procesos_por_seccion/' + seccion_id,
      success: function(result){
        $('#proceso').empty().html(result);
      }
    });  
}


$(document).on('change', '#ds', function(){
    texto = $(this).find('option:selected').attr('data-text');
    $('#ds-content').html(texto);
});

$(document).on('change', '#di', function(){
    texto = $(this).find('option:selected').attr('data-text');
    $('#di-content').html(texto);
});



/**************************************************************************/

//estas funciones son para bloquear el largo de los inputs number, ocupa el attr maxlength del input
function maxLengthCheck(object) {
  if (object.value.length > object.maxLength)
    object.value = object.value.slice(0, object.maxLength)
}
  
function isNumeric (evt) {
  var theEvent = evt || window.event;
  var key = theEvent.keyCode || theEvent.which;
  key = String.fromCharCode (key);
  var regex = /[0-9]|\./;
  if ( !regex.test(key) ) {
    theEvent.returnValue = false;
    if(theEvent.preventDefault) theEvent.preventDefault();
  }
}

/**************************************************************************/



  $('.delete-button').on('click', function(event){
      event.preventDefault();
      url = $(this).attr('href');
      ConfirmAlert(url);
  });


  function ConfirmAlert(Url){
      $.confirm({
          title: 'Alerta!',
          confirmButton: 'Si',
          cancelButton: 'NO',
          confirmButtonClass: 'btn btn-info',
          cancelButtonClass: 'btn btn-danger',
          dialogClass: "modal-dialog modal-lg",
          content: 'Esta seguro que desea eliminar éste registro?',
          icon: 'fa fa-warning',
          confirm: function(){
            window.location = Url;
          },
          cancel: function(){
            return;
          }
      });  
  }


  $(document).on('click', '.asignar-equipo-comunidad', function(){
    var valor = $(this).attr('data-id');
    var comunidad = $('#tabla-comunidad-asociar').attr('data-id');
    if($(this).prop("checked")){
        url = APP_URL + '/general/asignar_equipos/' + valor + '/' + comunidad;
    } else {
      url = APP_URL + '/general/eliminar_equipos/' + valor + '/' + comunidad
    }
      $.ajax({
        type: 'get',
        url:  url,
        success: function(res){

        }
      }); 
  });