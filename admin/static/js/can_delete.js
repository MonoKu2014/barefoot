
function can_delete(url,id,nombre,assoc,url_final){


   var _c=confirm('Estas Seguro(a) de Eliminar '+nombre);
   if(_c){

       $.post(url+'/'+id,function(data,status){

           if(data==0){
               window.location.href = url_final;
           }else{
               alert('No puede eliminarse '+nombre+' , porque existen '+assoc+' en el(la)');

           }

       });
   }else{


       return false;
   }


}
