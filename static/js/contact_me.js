 
/*
  Jquery Validation using jqBootstrapValidation
   example is taken from jqBootstrapValidation docs 
  */
$(function() {

    $("input,textarea").jqBootstrapValidation({
        preventSubmit: true,
        submitError: function($form, event, errors) {
            // something to have when submit produces an error ?
            // Not decided if I need it yet
        },
        submitSuccess: function($form, event) {
            event.preventDefault(); 
            $.ajax({
                url: "../contacts/send_request/",
                type: "POST",
                data: $form.serialize(),
                cache: false,
                success: function(data) {
                	$('#contactModal').modal('hide');
                  	$form.trigger("reset");
                  	$('#contactModalsend .modal-body').html(data);
                  	$('#contactModalsend .modal-title').html('Сообщение отправлено');
	                $('#contactModalsend').modal('show');
	                setTimeout(function() {
	                	$('#contactModalsend').modal('hide');
	                }, 3000);
                },
                error: function(data) {
                	// сделать вывод ошибки
                },
            })
        },
        filter: function() {
            return $(this).is(":visible");
        },
    });

    $("a[data-toggle=\"tab\"]").click(function(e) {
        e.preventDefault();
        $(this).tab("show");
    });
});


/*When clicking on Full hide fail/success boxes */
$('#name').focus(function() {
    $('#success').html('');
});