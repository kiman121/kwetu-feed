$(document).ready(function () {
    $(document).on("click", ".add-new-post", function (e) {
        e.preventDefault();
        $("#add_new_post").modal("show");
    });

    $(document).on("click", ".delete-post", function(e){
        e.preventDefault()

        var postId = $(this).parents(".blog-post").data('postid')
        $(".selected-post-delete").val(postId)
        $("#delete_post").modal("show");
    });

    $(document).on("click", ".btn-modal-dismiss", function(e){
        $(this).parents('.modal').modal('toggle');
    });
    
    $(document).on("click", ".edit-post", function(e){
        e.preventDefault()
        // Get post values
        var postId = $(this).parents(".blog-post").data('postid'),
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

    $(document).on("click", ".add-comment", function(e){
        e.preventDefault()

        var postId = $(this).parents(".blog-post").data('postid')
            userAuthStatus = $(this).data('userstatus');
        if (userAuthStatus === "not authenticated"){
            $("#user_prompt").modal("show");
        } else {
            $(".selected-post-comment").val(postId)
            $("#add_comment").modal("show");  
        }    
    });

    $(document).on("click", ".delete-comment", function(e){
        e.preventDefault()

        var commentId = $(this).parents(".comments-wrapper").data('commentid');
            $(".selected-comment-delete").val(commentId)
            $("#delete_comment").modal("show"); 
    });

    $(document).on("click", ".edit-profile", function(e){
        e.preventDefault()

        var fname = $(this).parents(".profile-box").find(".fname").val(),
            onames = $(this).parents(".profile-box").find(".onames").val(),
            bio = $(this).parents(".profile-box").find(".bio").val();
        
        $("form.form-edit-profile #first_name").val(fname);
        $("form.form-edit-profile #other_names").val(onames);
        console.log(bio)
        if (bio !== "None"){
            $("form.form-edit-profile #bio").val(bio);
        }
        
        $("#edit_profile").modal("show"); 
    });

    $(document).on("click", ".view-user-profile", function(e){
        e.preventDefault()
        var userAuthStatus = $(this).data('userstatus');
        console.log(userAuthStatus)
        if (userAuthStatus === "authenticate"){
            $("#user_prompt").modal("show");
        }
    });

    $(document).on("click", ".new-subscription", function(e){
        e.preventDefault()

        $("#add_subscription").modal("show");
    });
});
