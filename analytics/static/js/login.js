$(document).ready(function() {

    $("#login_form").submit(function() {
        $("#id_username").val($("#usernameInput").val());
        $("#id_password").val($("#passwordInput").val());
    });

});