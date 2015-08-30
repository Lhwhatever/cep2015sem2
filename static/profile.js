activate1 = function() {
    $('#edit-profile').click(function(e) {
        e.preventDefault();
        formid = $(this).parent().attr('id');

        $.ajax({
            type: 'POST',
            url: '/accounts/profile/',
            dataType: 'json',
            data: {
                'form_key': 'edit_profile',
                'about_me': $('#id_about_me').val(),
                'username': $('#id_username').val(),
                'email': $('#id_email').val(),
                'password': $('#id_password').val()
            },
            success: function(data) {
                if(data.status == 0) {
                    $('#editResponse').addClass('alert-danger');
                    $('#editResponse').html("<h5>Errors submitting form:</h5>" + data.message);
                    $('#editResponse').show();
                } else if(data.status == 1) {
                    $('#editModal').modal('hide');
                    messages.addSuccess(data.message);
                    $('#user_show').html(data.instance.username);
                    $('#email_show').html(data.instance.email);
                    $('#about_me_show').html(data.instance.about_me);
                }
            },
            crossDomain: false,
            beforeSend: function(xhr, settings) {
                if(!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        return false;
    });


}

activate2 = function() {
    $('#change-pw').click(function(e) {
        e.preventDefault();
        formid = $(this).parent().attr('id');

        $.ajax({
            type: 'POST',
            url: '/accounts/profile/',
            dataType: 'json',
            data: {
                'form_key': 'change_pw',
                'old_password': $('#id_old_password').val(),
                'password1': $('#id_password1').val(),
                'password2': $('#id_password2').val()
            },
            success: function(data) {
                if(data.status == 0) {
                    $('#changeResponse').addClass('alert-danger');
                    $('#changeResponse').html("<h5>Errors submitting form:</h5>" + data.message);
                    $('#changeResponse').show();
                } else if(data.status == 1) {
                    a = window.location.href.split('/');
                    window.location.replace(a.slice(0, a.length-2).join());
                }
            },
            crossDomain: false,
            beforeSend: function(xhr, settings) {
                if(!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        return false;
    });
}