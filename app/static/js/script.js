$(document).ready(function() {
    let inputCount = 1;

    $('#addInput').click(function() {
        $('#inputContainer').append(`<input type="text" name="name${inputCount}" placeholder="Name">`);
        inputCount++;
    });

    $('#dynamicForm').submit(function(event) {
        event.preventDefault();
        let formData = $(this).serializeArray();
        $.ajax({
            type: 'POST',
            url: '/save_form_data',
            data: formData,
            success: function(response) {
                console.log(response);
            }
        });
    });
});
