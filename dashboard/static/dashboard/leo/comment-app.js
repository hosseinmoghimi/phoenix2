
    // comments = comments
    // page_id = page_id
    // add_comment_url = add_comment_url
    // delete_comment_url = delete_comment_url

    // profile_id = profile_id
    // comment_template = comment_template


    // let comments = JSON.parse(`{{comments_s|escapejs}}`)
    // let page_id = parseInt("{{page.id}}")
    // let add_comment_url = "{% url 'dashboard:add_comment' %}"
    // let delete_comment_url = "{% url 'dashboard:delete_comment' %}"
 
    // let profile_id = parseInt("{{profile.id}}")
    // var comment_template = `{% include 'material/includes/comment.html' %}`
 
 
 let comment_component = Vue.component('comment-component', {
    data: function () {
        return {
            confirm_delete_comment: false,

            profile_id: profile_id
            // current_profile_id: JSON.parse("{% if profile %}{{profile.id}}{%else%}0{%endif%}")
        }
    },
    methods: {
        ShowConfirmDeleteComment: function () {

            this.confirm_delete_comment = true
        },
        ConfirmDeleteComment: function (comment_id) {


            this.confirm_delete_comment = false
            let url = delete_comment_url
            let posting = $.post(url, {
                comment_id: comment_id,
                csrfmiddlewaretoken: csrfmiddlewaretoken
            })

            posting.done(function (data) {
                console.log(data)
                if (data.result === 'SUCCEED') {
                    comment_app.comments=data.comments
                }
            })


        },
        CancelDeleteComment: function () {
            this.confirm_delete_comment = false
        },
    },
    props: ['comment'],
    template: comment_template,
})




let comment_app = new Vue({
    el: "#comment-app",
    data: {
        text: '',
        comments: comments,
        confirm_delete_comment: false,

    },
    methods: {

        add_comment: function () {



            let url =add_comment_url

            var posting = $.post(url,
                {
                    page_id: page_id,
                    text: comment_app.text,
                    csrfmiddlewaretoken: csrfmiddlewaretoken
                }
            );

            // Put the results in a div
            posting.done(function (data) {
                console.log(data)

                if (data.result === 'SUCCEED') {
                    // swal({
                    //     title: "ارسال نظر",
                    //     text: "نظر شما با موفقیت ارسال شد.",
                    //     buttonsStyling: false,
                    //     confirmButtonClass: "btn btn-success",
                    //     type: "success"
                    // }).catch(swal.noop)

                    comment_app.comments=(data.comments)
                    comment_app.text = ''
                }
            })


        },
    },
})




