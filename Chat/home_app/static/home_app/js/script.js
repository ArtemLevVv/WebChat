document.addEventListener('DOMContentLoaded', () => {
    const editButtons = document.querySelectorAll('.edit-post');

    editButtons.forEach(button => {
        button.addEventListener('click', () => {
            const postId = button.id;
            const modal = document.querySelector(`.modal-window-${postId}`);

            if (modal) {
                if (modal.style.display === 'flex') {
                    modal.style.display = 'none';
                } else {
                    modal.style.display = 'flex';
                }
            }
        });
    });
});
