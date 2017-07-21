

function confirmNewLocation() {

    $("#id_new_nip_name").val($("#newNipName").val());
    $("#id_new_nip_location_pk").val($("#newNipLocationDropdown").val());
    
    setSubmitButtonForm("submit_add_nip_form");

    $("#addNipModal").modal("hide");

    setConfirmationModalText(
        "Confirm New Nip",
        "Are you sure you want to create a new nip with the name <b>" + $("#newNipName").val() + "</b>" +
        " to monitor the location <b>" + $("#newNipLocationDropdown").text() + "</b>"
    );

    $("#confirmationModal").modal("show");

}

$(document).ready(function() {

    $("#openAddNip").click(function() {
        $("#addNipModal").modal("show");
    });

    $("#acceptNewNip").click(function() {
        confirmNewLocation();
    });


    $("#confirmationModal").on(
        "click",
        ".submit_add_nip_form",
        function() {
            $(this).attr("name", "add_nip_form");
            $(this).attr("form", "add_nip_form");
            $("#add_nip_form").submit();
        }
    );

});