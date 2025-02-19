import re
import logging

class URLShortener:
    def __init__(self, max_length=50):
        """
        Initialize the URLShortener with a max_length for displayed URLs.
        """
        self.max_length = max_length
    
    def shorten(self, url: str) -> str:
        """
        Shortens a given URL while keeping its main components.
        
        How It Works:
        - If the URL length is less than or equal to max_length, it remains unchanged.
        - If the URL exceeds max_length, it:
          1. Extracts the domain (e.g., https://www.amazon.in)
          2. Trims the path while ensuring the total length doesn't exceed max_length
          3. Adds '...' at the end to indicate shortening
        """
        if len(url) <= self.max_length:
            return url  # No need to shorten
        
        match = re.match(r'(https?://[^/]+)(/?.*)', url)
        if match:
            domain = match.group(1)  # Keep the domain
            path = match.group(2)[:self.max_length - len(domain) - 3]  # Trim path
            return f"{domain}{path}..."  # Append '...' to indicate shortening
        
        return url  # Return original if no match
    
    def log_shortened(self, message: str) -> str:
        """
        Automatically shortens URLs found in the log message.
        """
        return re.sub(r'https?://\S+', lambda match: self.shorten(match.group()), message)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    from my_package.url_shortener import URLShortener
    
    shortener = URLShortener()
    long_url = "https://www.amazon.in/Samsung-Smartphone-Titanium-Whitesilver-Included/dp/B0DSKL9MQ8/ref=sr_1_1_sspa?nsdOptOutParam=true&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY"
    
    # Logging with shortened URL
    log_message = f"Scraped URL: {long_url}"
    logger.info(shortener.log_shortened(log_message))
