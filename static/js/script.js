document.addEventListener('DOMContentLoaded', function () {
    const logo = document.getElementById('logo');

    logo.addEventListener('click', function () {
        // When the logo is clicked, submit the form
        const form = document.getElementById('blogForm');
        form.target = '_blank';  // Open in a new tab
        form.submit();
    });
});
