$(document).ready(function() {

    $(".dropdownOption").click(function() {
        $(this).parent().parent()
            .find("button")
                .text($(this).text())
                .val($(this).attr("id"));
    });

});