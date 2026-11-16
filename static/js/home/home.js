document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("novelSearchBtn");
    const input = document.getElementById("novelSearchInput");
    const feedback = document.getElementById("searchFeedback");
    if (!button || !input || !feedback) return;
    button.addEventListener("click", () => {
        feedback.textContent = input.value.trim()
            ? "Live search is coming soon. Your collection is shown on the left."
            : "Enter a title, author, or tag to preview search.";
        input.focus();
    });
    input.addEventListener("keydown", (event) => {
        if (event.key === "Enter") { event.preventDefault(); button.click(); }
    });
});
