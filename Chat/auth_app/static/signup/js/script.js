document.getElementById("code-form").addEventListener("click", function () {
    const container = document.getElementById("code-form-container");

    container.innerHTML = `
        <form method="post" action="/auth/verify-email/">
            <input type="hidden" name="csrfmiddlewaretoken" value="{{ csrf_token }}">
            <label>Введіть код підтвердження:</label>
            <input type="text" name="email_code" required />
            <button type="submit">Підтвердити</button>
        </form>
    `;
});