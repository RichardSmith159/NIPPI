

$(document).ready(function() {

    $(".removeSiren").click(function() {

        var sirenPK = $(this).parent().parent().attr("id").replace("siren_", "");

        $("#id_delete_siren_pk").val(sirenPK);

        $("#confirmDeleteSiren").modal("show");

    });

});