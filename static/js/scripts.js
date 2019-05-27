window.onload = function () {
    console.log("DOM loaded");


    $("#edit-uploaded-button").on("click",  function (event) {
        if ($(".image-button").css("display") == "none") {
            $(".image-button").css("display", "inline-block");
            $("#edit-uploaded-button").text("Завершить редактировать");
        } else {
            $(".image-button").css("display", "none");
            $(".place-edit-form").css("display", "none");
            $("#edit-uploaded-button").text("Редактировать новость");

        }
        event.preventDefault();
    });

    $(".place-sort-menu select").on("change", function (event) {
        var selectedValue = event.target.value;
        window.location = "/places/order/set/" + selectedValue + "/";
    });
}

function editPlace(pk) {
    $.ajax({
        url: "/place/edit/" + pk + "/ajax/",
        success: function (answer) {
            $("#place-edit-form-" + answer.pk).html(answer.form);
            $("#place-edit-form-" + answer.pk).css("display", "block");
        },
    });

function openForm() {
  document.getElementById("myForm").style.display = "block";
}
function closeForm() {
  document.getElementById("myForm").style.display = "none";
}


}

