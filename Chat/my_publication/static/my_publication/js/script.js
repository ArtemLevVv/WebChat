document.querySelectorAll('.edit-post').forEach(button => {
    let show_window = false;
    
    button.addEventListener('click', () => {
        show_window = !show_window;

      // Контейнер тексту, який відповідає цьому посту
        const postDiv = button.closest('.posts');
        const container = postDiv.querySelector('.text');

      // Якщо вже є блок - видалити
        const existingCon = container.querySelector('.edit-controls');
        if (existingCon) {
        existingCon.remove();
        }

        if (show_window) {
        // Створюємо блок з кнопками
        const con = document.createElement('div');
        con.classList.add('edit-controls');  // клас для стилізації, щоб потім легко знайти

        const conButtonEdit = document.createElement('button');
        conButtonEdit.textContent = 'Редагувати допис';

        const conButtonDelete = document.createElement('button');
        conButtonDelete.textContent = 'Видалити публікацію';

        con.appendChild(conButtonEdit);
        con.appendChild(conButtonDelete);

        container.appendChild(con);
        }
    });
});
