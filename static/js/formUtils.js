

function setSubmitButtonForm(uniqueFormSubmissionClass) {
    $("#confirm")
        .removeClass()
        .addClass("btn acceptButton")
        .addClass(uniqueFormSubmissionClass);
}