


function confirmNewLocation() {

    $("#id_new_location_name").val($("#newLocationName").val());
    
    setSubmitButtonForm("submit_add_location_form");

    $("#addLocationModal").modal("hide");

    setConfirmationModalText(
        "Confirm New Location",
        "Are you sure you want to create a new location with the name <b>" + $("#newLocationName").val() + "</b> ?"
    );

    $("#confirmationModal").modal("show");

}


$(document).ready(function() {
    
    $(".openDeleteLocation").click(function() {

        var locationPK = $(this).parent().parent().attr("id");
        var locationName = $(this).parent().parent().find(".nameCell").html();

        $("#id_location_pk_for_deletion").val(locationPK);
        
        setSubmitButtonForm("submit_delete_location_form");
        setConfirmationModalText(
            "Confirm Location Deletion",
            "Are you sure you want to delete the location " + locationName + "?"
        );

        $("#confirmationModal").modal("show");

    });


    $("#openAddLocation").click(function() {
        $("#addLocationModal").modal("show");
    });

    $("#acceptNewLocation").click(function() {
        confirmNewLocation();
    });

    $("#confirmationModal").on(
        "click",
        ".submit_add_location_form",
        function() {
            $(this).attr("name", "add_location_form");
            $(this).attr("form", "add_location_form");
            $("#add_location_form").submit();
        }
    );

    $("#confirmationModal").on(
        "click",
        ".submit_delete_location_form",
        function() {
            $(this).attr("name", "delete_location_form");
            $(this).attr("form", "delete_location_form");
            $("#delete_location_form").submit();
        }
    );

});