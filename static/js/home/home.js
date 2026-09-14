// Home feature client script
document.addEventListener("DOMContentLoaded", () => {
    const searchBtn = document.getElementById("novelSearchBtn");
    const searchInput = document.getElementById("novelSearchInput");

    if (searchBtn && searchInput) {
        searchBtn.addEventListener("click", () => {
            const query = searchInput.value.trim();
            if (!query) {
                alert("Please enter a novel title or keyword to search.");
                searchInput.focus();
                return;
            }
            alert(`Searching for: "${query}" (Feature coming soon)`);
        });
        
        searchInput.addEventListener("keypress", (e) => {
            if (e.key === "Enter") {
                searchBtn.click();
            }
        });
    }
});
