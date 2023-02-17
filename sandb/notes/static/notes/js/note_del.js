$(document).on('click', '.delete-post', function() {
    var postId = $(this).data('post-id');
    $.ajax({
        type: 'POST',
        url: '/delete-note/',
        data: {
            'post_id': postId,
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        success: function() {
            // Удаление поста успешно завершено. Обновляем содержимое страницы.
            location.reload();
        }
    });
});
