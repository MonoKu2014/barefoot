$(document).ready(function(){

    $("input[type='file']").change(function(nombre){
         var errors=0
        $("input[type='file']").each(function() {
            var filename = $(this).val();
            if(filename.trim()!="" && filename!=undefined ) {
            var _ext = filename.split('.')
            var ext=_ext[_ext.length-1]


                if (ext != 'pdf' && ext != 'doc' && ext != 'docx') {
                    input_div = $(this).parents('div').next().children(".error").html('Formato no Soportado');
                    errors++;

                } else {
                    input_div = $(this).parents('div').next().children(".error").html('');

                }
                console.log("tester")
            }

        });
        if(errors>0){$('#submit_btn').attr('disabled', 'disabled');}else{$('#submit_btn').removeAttr('disabled');}

    });

   $('.fa-file-word-o,.fa-file-pdf-o').each(function(){

       var input_div=$(this).parents('div').prev().children("input[type='file']");
       input_div.css('color','transparent')


   })

    $('#submit_btn').click(function(){

       $('#form_comunidad,#form_equipo').submit();

    });

});