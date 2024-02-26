# EMAILify

EMAILify is a Python-based project designed to extract email addresses from pages quickly. Whether you need to gather contact information for networking, lead generation, or research purposes, Email-ify simplifies the process by providing a user-friendly WebUI and a convenient API.


## Features

- **WebUI**: Accessible through a web browser, the WebUI allows users to input a valid URL and receive a list of extracted email addresses from the corresponding website.
- **API**: For seamless integration into existing applications or workflows, Email-ify offers an API endpoint that accepts URL parameters, making it easy to automate email extraction processes.

## Usage

### WebUI

To extract email addresses using the WebUI, follow these steps:

1. Navigate to the URL: [http://localhost:8000/](http://localhost:8000/) in your web browser.
2. Input a valid URL into the provided field.
3. Click the "Extract Emails" button.
4. View the extracted email addresses displayed on the screen.

### API

To utilize the API for email extraction programmatically, follow these steps:

1. Make a GET request to the API endpoint with the `url` parameter set to the target URL.
2. Receive a JSON response containing the extracted email addresses.

Example API request:
```url
http://localhost:8000/api/?url=URLHERE
```

Example API response:
```json
{
    "status": "success",
    "emails": ["contact@****.com", "info@****.com", "license@****.com", "tech@****.com"]
}
```

## Requirements

Ensure you have the following dependencies installed:

- Django >= 5.0.2
- requests >= 2.31.0

Install the dependencies using pip:
```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enhance Email-ify.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
``` ````
