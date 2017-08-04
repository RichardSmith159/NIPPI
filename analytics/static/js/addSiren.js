

$(document).ready(function() {

    $(".addSiren").click(function() {
        $("#addSirenModal").modal("show");
    });

    $("#confirmSirenCreation").click(function() {

        $("#id_name").val($("#newSirenName").val());
        if ($("#newSirenVariable").val() == "") {
            $("#id_monitor_variable").val("temperature");
        } else {
            $("#id_monitor_variable").val($("#newSirenVariable").val());
        }
        if ($("#newSirenTolerance").val() > 0) {
            $("#id_tolerance").val(3);
        } else {
            $("#id_tolerance").val($("#newSirenTolerance").val());
        }
        
        $("#id_acceptable_bounds_upper_limit").val($("#newSirenUpperLimit").val());
        $("#id_acceptable_bounds_lower_limit").val($("#newSirenLowerLimit").val());
        
        if ($("#newSirenMessage") == "") {
            $("#id_message").val("Monitored variable out of bounds.");
        } else {
            $("#id_message").val($("#newSirenMessage").val());
        }
        
        if ($("#newSirenEmailEnabled").is(":checked")) {
            $("#id_email_notification").val(True);
        }

        if ($("#newSirenTextEnabled").is(":checked")) {
            $("#id_text_notification").val(True);
        }
        
        $("#add_siren_form").submit();

    });

});