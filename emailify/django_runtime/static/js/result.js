function goBack() {
    window.history.back();
}

function copyToClipboard(email) {
    // Create a temporary input element
    var tempInput = document.createElement("input");
    // Assign the email value to the input element
    tempInput.value = email;
    // Append the input element to the document body
    document.body.appendChild(tempInput);
    // Select the input element's content
    tempInput.select();
    // Copy the selected content to the clipboard
    document.execCommand("copy");
    // Remove the temporary input element
    document.body.removeChild(tempInput);
    // Provide feedback to the user (optional)
    alert("Email copied to clipboard: " + email);
}