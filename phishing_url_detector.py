import re
from urllib.parse import urlparse

def is_phishing_url(url):
    # First, basic check: does it look like a URL?
    try:
        parsed = urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            return "Suspicious"  # not a valid URL
    except:
        return "Suspicious"
    
    score = 0
    
    # URL length
    if len(url) > 75:
        score += 1
    
    # HTTPS check
    if not url.startswith("https"):
        score += 1
    
    # @ symbol in URL
    if "@" in url:
        score += 1
    
    # IP address instead of domain
    domain = parsed.netloc
    if re.match(r'\d+\.\d+\.\d+\.\d+', domain):
        score += 1
    
    # Hyphens in domain
    if '-' in domain:
        score += 1
    
    # If score >= 2 OR URL is too short/invalid → suspicious
    if score >= 2:
        return "Suspicious"
    
    return "Safe"
