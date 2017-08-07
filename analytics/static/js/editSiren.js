
function getSirenDetailsForEdit(sirenPK) {
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

        $("#id_edit_siren_pk").val(sirenPK);

        getSirenDetailsForEdit(sirenPK);

    });

    $("#acceptEditSiren").click(function() {


        if ($("#editSirenName").val()) {
            $("#id_edit_siren_name").val($("#editSirenName").val());
        }
        if ($("#editSirenVariable").val()) {
            $("#id_edit_siren_monitor_variable").val($("#editSirenVariable").val());
        }

        if ($("#editSirenTolerance").val()) {
            $("#id_edit_siren_tolerance").val($("#editSirenTolerance").val());
        }

        if ($("#editSirenUpperLimit").val()) {
            $("#id_edit_siren_acceptable_bounds_upper_limit").val($("#editSirenUpperLimit").val());
        }
        if ($("#editSirenLowerLimit").val()) {
            $("#id_edit_siren_acceptable_bounds_lower_limit").val($("#editSirenLowerLimit").val());
        }
        if ($("#editSirenMessage").val()) {
            $("#id_edit_siren_edit_siren_message").val($("#editSirenMessage").val());
        }
        
        if ($("#editSirenEmailEnabled").is(":checked")) {
            $("#id_edit_siren_email_notification").val("Y");
        } else {
            $("#id_edit_siren_email_notification").val("N");
        }
        if ($("#editSirenTextEnabled").is(":checked")) {
            $("#id_edit_siren_text_notification").val("Y");
        } else {
            $("#id_edit_siren_text_notification").val("N");
        }

        $("#editSirenModal").modal("hide");
        $("#confirmSirenEditModal").modal("show");

    });

});