$(document).ready(function () {
    $(document).on("click", ".add-new-post", function (e) {
        e.preventDefault();
        $("#add_new_post").modal("show");
    });

    $(document).on("click", ".delete-post", function(e){
        e.preventDefault()

        var postId = $(this).data('postid')
        $(".selected-post-delete").val(postId)
        $("#delete_post").modal("show");
    });

    $(document).on("click", ".btn-modal-dismiss", function(e){
        $(this).parents('.modal').modal('toggle');
    });
    
    $(document).on("click", ".edit-post", function(e){
        e.preventDefault()
        // Get post values
        var postId = $(this).data('postid'),
            categorId = parseInt($(this).parents('.blog-post').find('.category-id').val()),
            postTitle = $(this).parents('.blog-post').find('.post-title').val(),
            postDetail = $(this).parents('.blog-post').find('.post-detail').val();

        // Set edit form values
        $("form.form-edit-post #category").val(categorId).change();
        $("form.form-edit-post #title").val(postTitle);
        $("form.form-edit-post #post").val(postDetail);
        $("form.form-edit-post .selected-post-edit").val(postId);

        // Open modal
        $("#edit_post").modal("show");

    });
});
