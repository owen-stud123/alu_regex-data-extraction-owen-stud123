import re

# Regular Expressions for 4 data types

def extract_emails(text):
    """Extracts all email addresses from the provided text."""
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}')
    return email_pattern.findall(text)

def extract_urls(text):
    """Extracts all URLs from the provided text."""
    url_pattern = re.compile(r'https?://[a-zA-Z0-9.-]+(?:\\.[a-zA-Z]{2,})+(?:/[a-zA-Z0-9./?=&-]*)?')
    return url_pattern.findall(text)

def extract_phone_numbers(text):
    """Extracts phone numbers in various formats from the provided text."""
    phone_pattern = re.compile(r'(\\(\\d{3}\\) \\d{3}-\\d{4}|\\d{3}[.-]\\d{3}[.-]\\d{4})')
    return phone_pattern.findall(text)

def extract_currency(text):
    """Extracts currency amounts from the provided text."""
    currency_pattern = re.compile(r'\\$\\d{1,3}(?:,\\d{3})*(?:\\.\\d{2})?')
    return currency_pattern.findall(text)

# Example text to test
text = """
Contact us at support@example.com or sales@company.co.uk.
Visit our site: https://www.example.com or https://subdomain.example.org/page.
Call (123) 456-7890 or 123-456-7890 for assistance.
Prices: $19.99, $1,234.56.
"""

if __name__ == "__main__":
    print("Emails:", extract_emails(text))
    print("URLs:", extract_urls(text))
    print("Phone Numbers:", extract_phone_numbers(text))
    print("Currency Amounts:", extract_currency(text))

