
function getSirenDetails(sirenPK) {
    $.ajax({
        url: "/analytics/get_siren_data/" + sirenPK,
        success: function(data) {

            $("#sirenDetailsModalTitle").text("Siren Details: " + data["name"]);

            $("#subList").empty();

            $("#sirenNameField").text(data["name"]);
            $("#sirenCreatorField").text(data["creator"]);
            $("#sirenMetricField").text(data["monitor_variable"]);
            $("#sirenToleranceField").text(data["tolerance"]);
            $("#sirenUpperLimitField").text(data["acceptable_bounds_upper_limit"]);
            $("#sirenLowerLimitField").text(data["acceptable_bounds_lower_limit"]);
            $("#sirenAlertMessageField").text(data["message"]);
            $("#sirenEmailField").text(data["email_notification"]);
            $("#sirenTextField").text(data["text_notification"]);

            for (var i= 0; i < data["registered_users"].length; i++) {
                $("#subList").append("<li class='registeredUser'>" + data["registered_users"][i] + "</li>")
            }

            $("#sirenDetailsModal").modal("show");

        }
    });
}


$(document).ready(function() {

    $(".openSirenDetails").click(function() {
        var sirenPK = $(this).parent().parent().attr("id").replace("siren_", "");

        getSirenDetails(sirenPK);

    });

});