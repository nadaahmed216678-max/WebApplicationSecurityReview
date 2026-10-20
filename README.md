# Web Application Security Code Review

## Project Description

This project is an educational security review of a simple web application built with Python and Flask.

The review focuses on common web security topics, including:

- Input validation
- Output escaping and XSS prevention
- Authentication and access control
- Debug mode configuration
- Error handling and information disclosure
- HTTP security headers
- Hardcoded secrets

## Technologies Used

- Python
- Flask
- HTML
- Visual Studio Code

## Project Structure

```text
WebSecurityReview/
├── app.py
├── security_review.md
└── templates/
    └── login.html
```

## Requirements

- Python 3
- Flask
- MarkupSafe

## How to Run

1. Open a terminal in the project directory.
2. Install the required packages if they are not already installed:

   ```bash
   python -m pip install Flask
   ```

3. Start the application:

   ```bash
   python app.py
   ```

4. Open the following address in your browser:

   `http://127.0.0.1:5000`

## Security Notes

This is a local educational application, not a production-ready authentication system.

The application does not currently verify passwords or implement authenticated sessions and access control. HTTP security headers are configured in the code, but their presence in HTTP responses remains unverified.

Do not deploy this training application publicly as a production service.

## Report

See `security_review.md` for the security findings, remediation steps, and verification status.
