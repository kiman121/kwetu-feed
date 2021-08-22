$(document).ready(function () {
    $(document).on("click", ".add-new-post", function (e) {
        e.preventDefault();
        $("#add_new_post").modal("show");
    });
});
