document.getElementById("scraper-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let status = document.getElementById("status");
    status.textContent = "Scraping images, please wait...";
    
    let formData = new FormData(this);
    fetch("/", {
        method: "POST",
        body: formData
    }).then(response => {
        if (response.ok) {
            return response.blob();
        }
        throw new Error("Network response was not ok.");
    }).then(blob => {
        let url = window.URL.createObjectURL(blob);
        let a = document.createElement("a");
        a.href = url;
        a.download = "images.zip";
        document.body.appendChild(a);
        a.click();
        a.remove();
        status.textContent = "Download complete!";
    }).catch(error => {
        console.error("Error:", error);
        status.textContent = "Failed to scrape images.";
    });
});