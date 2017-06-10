$(document).ready(function(){


$('#save_sup').click(function(){

  var final_ids="";
  $(".subm:checked").each(function(){

    var value=$(this).prev(".ids").val();
    final_ids+=value+"_"

  })
  final_ids=final_ids.substring(0,final_ids.length-1)
  $("#submodulos_ids").val(final_ids)
  $("#formulario_final").submit()

})
});
