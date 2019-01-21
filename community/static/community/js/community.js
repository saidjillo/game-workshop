$(document).ready(function(){
  
    var posts = $('.btn-replying');

    posts.each( function(index, obj) {
        var count = 0;
        var post = $(this);
        post.click( function(e) {
            count++; 
            
            posts.each( function(index, obj) {                 
                $(posts[index]).parent().parent().find('.form-enter').hide();               
            });

            var reply_form = post.parent().parent().find('.form-enter');           
            // check if it was clicked earlier
            if( count % 2 !== 0 ) {
                $(reply_form).show(); 
                handle_reply_submission();
               
            }else if(count % 2 == 0 ) {            
                $(reply_form).hide();             
            }

            function handle_reply_submission(){
                reply_form.find('form').submit( function(e) {
                    e.preventDefault();

                    var textaera = reply_form.find('form').find('#areaReply');
                    var forum_pk = $('#forum_pk').val();
                    var post_pk  = reply_form.find('input[type=hidden].the-post').val();
                  
                    if (textaera.val().trim() == ""){
                        textaera.css("box-shadow", "0 0 4px #811");

                    }else{
                        // handle ajax request
                        var act_text = textaera.val();
                        var url = post.attr('data-ajax-target')
                        ajax_request(forum_pk,post_pk, act_text, url, reply_form);
                    }

                    
                });
            }
            
        });
    });


    // ajax 
    function ajax_request(forum_pk,post_pk, reply, urlto, post) {
        $.ajax({          
            type:  'POST',
            url :  urlto,
            data: {
                'forum_pk':forum_pk,
                'post_pk':post_pk,
                'reply':reply
            },
            async:true,
            dataType: 'html',
            success: function(response_data) {
                parent_post = post.parent().find('.forum-post').find('.all-post-replies')
                parent_post.prepend(response_data);
            },
            error: function(XMLHttpRequest,textStatus,errorThrown) {
            }
       });
    }

});