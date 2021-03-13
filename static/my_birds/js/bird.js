$(".js-create-bird").click(function () {
    $.ajax({
      url: '/bird/create/',
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-bird").modal("show");
      },
      success: function (data) {
        $("#modal-bird .modal-content").html(data.html_form);
      }
    });
  });