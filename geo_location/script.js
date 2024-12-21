// Function to get geolocation and store it in localStorage
function storeLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(storeLocationInLocalStorage, showError);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

// Store location in localStorage
function storeLocationInLocalStorage(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    const location = {
        latitude: latitude,
        longitude: longitude,
    };

    // Store the location object in localStorage
    localStorage.setItem("userLocation", JSON.stringify(location));
}

// Handle geolocation errors
function showError(error) {
    switch (error.code) {
        case error.PERMISSION_DENIED:
            alert("User denied the request for Geolocation.");
            break;
        case error.POSITION_UNAVAILABLE:
            alert("Location information is unavailable.");
            break;
        case error.TIMEOUT:
            alert("The request to get user location timed out.");
            break;
        case error.UNKNOWN_ERROR:
            alert("An unknown error occurred.");
            break;
    }
}

// Call the storeLocation function when the page loads
window.onload = storeLocation;

// Function to launch the camera and preview the photo
function launchCamera() {
    const input = document.createElement("input");
    input.type = "file";
    input.accept = "image/*";
    input.capture = "environment";
    input.onchange = (event) => {
        const file = event.target.files[0];
        if (file) {
            addPhoto(file);
        }
    };
    input.click();
}

// Add a new photo to the gallery
function addPhoto(file) {
    const gallery = document.createElement("div");
    gallery.classList.add("photo-container");

    const img = document.createElement("img");
    img.src = URL.createObjectURL(file);
    img.alt = "Photo Preview";
    img.classList.add("photo-preview");

    const statusContainer = document.createElement("div");
    statusContainer.classList.add("status-container");

    const upvoteCount = document.createElement("span");
    upvoteCount.textContent = "Upvotes: 0";
    upvoteCount.classList.add("upvote-count");

    const donationTotal = document.createElement("span");
    donationTotal.textContent = "Donations: ₹0";
    donationTotal.classList.add("donation-total");

    const optionsContainer = document.createElement("div");
    optionsContainer.classList.add("options-container");

    const upvoteButton = document.createElement("button");
    upvoteButton.textContent = "Upvote";
    upvoteButton.classList.add("action-button");
    upvoteButton.onclick = () => upvotePhoto(upvoteButton, upvoteCount);

    const donateButton = document.createElement("button");
    donateButton.textContent = "Donate";
    donateButton.classList.add("action-button");
    donateButton.onclick = () => donatePhoto(donationTotal);

    // Cross icon for removing photo
    const removeIcon = document.createElement("span");
    removeIcon.classList.add("remove-icon");
    removeIcon.innerHTML = "&times;";  // Using HTML entity for the cross symbol
    removeIcon.onclick = () => removePhoto(gallery);

    statusContainer.append(upvoteCount, donationTotal);
    optionsContainer.append(upvoteButton, donateButton);
    gallery.append(removeIcon, img, statusContainer, optionsContainer);
    document.body.appendChild(gallery);
}

// Remove a photo from the gallery
function removePhoto(photoContainer) {
    photoContainer.remove();
}

// Handle upvotes for a specific photo
function upvotePhoto(button, countElement) {
    let count = parseInt(countElement.textContent.split(": ")[1]);
    count++;
    countElement.textContent = `Upvotes: ${count}`;
    button.disabled = true;
    button.textContent = "Upvoted!";
}

// Handle donations for a specific photo
function donatePhoto(donationElement) {
    const amount = prompt("Enter the amount you wish to donate (in ₹):");
    if (amount && !isNaN(amount) && Number(amount) > 0) {
        let total = parseInt(donationElement.textContent.split("₹")[1]);
        total += Number(amount);
        donationElement.textContent = `Donations: ₹${total}`;
        alert(`Thank you for your donation of ₹${amount}!`);
    } else {
        alert("Please enter a valid donation amount.");
    }
}
