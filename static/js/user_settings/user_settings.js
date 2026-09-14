// User settings client-side enhancements
document.addEventListener('DOMContentLoaded', () => {
    const darkModeToggle = document.getElementById('darkModeToggle');

    if (darkModeToggle) {
        darkModeToggle.addEventListener('change', (e) => {
            // Provide subtle instant UI feedback
            if (e.target.checked) {
                document.body.style.backgroundColor = '#070b14';
            } else {
                document.body.style.backgroundColor = '#0b1120';
            }
        });
    }
});
