function confirmNewUser() {

    $("#id_new_username").val($("#newUserUsername").val());
    $("#id_new_email").val($("#newUserEmail").val());
    
    setSubmitButtonForm("submit_add_user_form");

    $("#addUserModal").modal("hide");

    setConfirmationModalText(
        "Confirm New User",
        "Are you sure you want to create a new user with the username <b>" +
            $("#newUserUsername").val() +
            "</b> and email <b>" +
            $("#newUserEmail").val() +
            "</b> ?"
    );

    $("#confirmationModal").modal("show");

}

$(document).ready(function() {

    $("#openAddUser").click(function() {
        $("#addUserModal").modal("show");
    });

    $("#acceptNewUser").click(function() {
        confirmNewUser();
    });

    
    $(".openDeleteUser").click(function() {
        
        $("#id_user_pk").val($(this).parent().parent().attr("id"));
    
        setSubmitButtonForm("submit_delete_user_form");

        setConfirmationModalText(
            "Confirm User Deletion",
            "Are you sure you want to delete the user <b>" +
                $(this).parent().parent().find(".usernameCell").html() +
                "</b> ?"
        );

        $("#confirmationModal").modal("show");

    });


    $("#confirmationModal").on(
        "click",
        ".submit_add_user_form",
        function() {
            $(this).attr("name", "add_user_form");
            $(this).attr("form", "add_user_form");
            $("#add_user_form").submit();
        }
    );
    
    $("#confirmationModal").on(
        "click",
        ".submit_delete_user_form",
        function() {
            $(this).attr("name", "delete_user_form");
            $(this).attr("form", "delete_user_form");
            $("#delete_user_form").submit();
        }
    );
});