

$(document).ready(function() {

    $("#profileIcon").click(function() {

        if ($(".profileDiv").hasClass("open")) {

            $(".profileDiv").removeClass("open");
            $(".profileDiv").fadeOut(75);

        } else {

            $(".profileDiv").addClass("open");
            $(".profileDiv").fadeIn(75);

        }
        
    });

});