# Bulk Email Sender

This Python script is designed to send bulk emails using the SMTP (Simple Mail Transfer Protocol) server. It leverages the `smtplib` library for email sending and `email` for creating email content. The script is intended for sending emails to multiple recipients with personalized content.

## Getting Started

### Prerequisites

- Python 3.x
- Access to an SMTP server (e.g., Gmail) for sending emails

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your_username/Bulk_Email.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Bulk_Email
   ```

3. Create a virtual environment:

   ```bash
   python3 -m venv .venv
   ```

4. Activate the virtual environment:

   ```bash
   source .venv/bin/activate
   ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Edit the `editable.py` file to set your SMTP server details, sender's email address, and password.

```python
#!/usr/bin/python3

smtp_server = "smtp.gmail.com"  # Update this with your SMTP server
sender_email = "sender@mail.com"  # Update this with your email address
sender_password = "sender password"  # Update this with your email password
```

### Usage

1. Add participants' details in the `resources/participants.py` file.

2. Customize the email subject and body in the `resources/body.html` file.

3. Run the script:

   ```bash
   ./send.py
   ```

## Contributing

Feel free to contribute by opening issues, providing feedback, or submitting pull requests. Any contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
