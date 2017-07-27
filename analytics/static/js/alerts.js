
$(document).ready(function() {

    $(".alertActionOption").click(function() {

        var alertPK = $(this).parent().parent().parent().parent().attr("id");

        if ($(this).text() == "Seen") {
            $("#seenModalTitle").text("Confirm Acknowledgement of Alert: " + alertPK);
            $("#seenModal").modal("show");
        }
        if ($(this).text() == "Handled") {
            $("#handledModalTitle").text("Confirm Acknowledgement of Alert: " + alertPK);
            $("#handledModal").modal("show");
        }
    });

    $("#confirmSeen").click(function() {
        $("#id_alert_pk").val($("#seenModalTitle").text().split(": ")[1]);
        alert($("#id_alert_pk").val());
        $("#id_seen").val(true);
        $("#respond_to_alert_form").submit();
    });

    $("#confirmHandled").click(function() {
        $("#id_alert_pk").val($("#handledModalTitle").text().split(": ")[1]);
        $("#id_handled").val(true);
        $("#respond_to_alert_form").submit();
        
    });

});