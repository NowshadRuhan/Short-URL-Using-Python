import pyshorteners

long_url = input("Enter the URL: ")
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)

print("Your Shortened URL is: " + short_url)