
function getSirenDetails(sirenPK) {
    $.ajax({
        url: "/analytics/get_siren_data/" + sirenPK,
        success: function(data) {

            $("#editSirenModalTitle").text("Edit Siren: " + data["name"]);
            $("#editSirenName").attr("placeholder", data["name"]);
            $("#editSirenVariable").attr("placeholder", data["monitor_variable"]);
            $("#editSirenTolerance").attr("placeholder", data["tolerance"]);
            $("#editSirenUpperLimit").attr("placeholder", data["acceptable_bounds_upper_limit"]);
            $("#editSirenLowerLimit").attr("placeholder", data["acceptable_bounds_lower_limit"]);
            $("#editSirenMessage").attr("placeholder", data["message"]);
            
            if (data["email_notification"]) {
                $("#editSirenEmailEnabled").prop("checked", true);
            } else {
                $("#editSirenEmailEnabled").prop("checked", false);
            }

            if (data["text_notification"]) {
                $("#editSirenTextEnabled").prop("checked", true);
            } else {
                $("#editSirenTextEnabled").prop("checked", false);
            }
            
            $("#editSirenModal").modal("show");

        }

    });

}

$(document).ready(function() {

    $(".openSirenEdit").click(function() {
        
        var sirenPK = $(this).parent().parent().attr("id").replace("siren_", "");
        getSirenDetails(sirenPK);

    });

    $("#acceptEditSiren").click(function() {

        $("#id_edit_siren_pk").val();
        $("#id_edit_siren_name").val();
        $("#id_edit_siren_monitor_variable").val();
        $("#id_edit_siren_tolerance").val();
        $("#id_edit_siren_acceptable_bounds_upper_limit").val();
        $("#id_edit_siren_acceptable_bounds_lower_limit").val();
        $("#id_edit_siren_edit_siren_message").val();
        $("#id_edit_siren_email_notification").val();
        $("#id_edit_siren_text_notification").val();



        $("#editSirenModal").modal("hide");
        $("#confirmSirenEditModal").modal("show");
    });

});