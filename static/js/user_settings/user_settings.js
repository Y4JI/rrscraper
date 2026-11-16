document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.getElementById('darkModeToggle');
    if (toggle) toggle.addEventListener('change', () => {
        document.body.dataset.theme = toggle.checked ? 'dark' : 'light';
    });
});
