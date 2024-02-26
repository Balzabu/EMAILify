function disappearUrlError() {
    setTimeout(() => {
    const box = document.getElementById('url-error-message');

      // removes element from DOM
      box.style.display = 'none';

    }, 2300); // time in milliseconds
}

function disappearEmailError() {
    setTimeout(() => {
    const box = document.getElementById('error-message');

      // removes element from DOM
      box.style.display = 'none';

    }, 2300); // time in milliseconds
}


function checkWebsite() {
    var urlInput = document.getElementById('url').value;
    document.getElementById('searchButton').disabled = true;

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "");

    // Get CSRF token from the meta tag
    var csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    // Include the CSRF token in the request headers
    xhr.setRequestHeader('X-CSRFToken', csrfToken);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    xhr.onload = function () {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.emails && response.emails.length > 0) {
                document.getElementById('searchButton').disabled = false;
                window.location.href = "/result?emails=" + encodeURIComponent(JSON.stringify(response.emails));
            } else {
                // Show the error message
                document.getElementById('error-message').style.display = 'block';
                disappearEmailError();
                document.getElementById('searchButton').disabled = false;
            }
        } else {
            alert("Error: " + xhr.statusText);
        }
    };
    xhr.onerror = function () {
        alert("Request failed.");
    };
    xhr.send("url=" + encodeURIComponent(urlInput));

    document.getElementById('searchButton').disabled = false;
}


// Stolen from stackoverflow.com :) https://stackoverflow.com/questions/1701898/how-to-detect-whether-a-string-is-in-url-format-using-javascript
function isUrl(s) {
   var regexp = /(http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/
   return regexp.test(s);
}

// Check if the URL provided is valid or not,else execute our main function
function checkForm(){
    var urlInput = document.getElementById('url').value;
    if(urlInput != "" && isUrl(urlInput)){
        checkWebsite();
        document.getElementById('searchButton').disabled = true;
        return false;
    }
    else{
        document.getElementById('url-error-message').style.display = 'block';
        disappearUrlError();
        return false;
    }
    document.getElementById('searchButton').disabled = false;
}