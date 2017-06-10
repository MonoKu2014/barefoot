(function() {
  $.ajaxSetup({
    headers: {
      'X-CSRF-TOKEN': $('#crsf').val()
    }
  });

  $(document).ready(function() {
    $(".accordion-toggle").click(function() {
      var parent;
      parent = $(this).parents(".panel-heading").next();
      if (parent.hasClass("collapse")) {
        return parent.removeClass("collapse").addClass("in");
      } else {
        return parent.removeClass("in").addClass("collapse");
      }
    });
    $(".accordion-toggle:first").trigger("click");
    return $(":checkbox[name='check']").change(function() {
      var _id, _perfil, _type, _url, sel;
      _type = $(this).parent().attr("id");
      _id = $(this).attr("id");
      _perfil = $(":hidden#id").val();
      _url = "/admin/perfiles/addRol";
      sel = $(this).prop("checked");
      if (sel === false) {
        _url = "/admin/perfiles/removeRol";
      }
      return $.ajax({
        url: _url + '/' + _id + '/' + _perfil + '/' + _type,
        method: 'POST',
        dataType: "html",
        success: function(data) {
          return console.log('tester');
        }
      });
    });
  });

}).call(this);