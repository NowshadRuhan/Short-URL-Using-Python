# Short-URL-Using-Python
Short Your URL Using Python

## Before Run this code install :
```
pip install pyshorteners
```

## Run this code
```
import pyshorteners

long_url = input("Enter the URL: ")
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)

print("Your Shortened URL is: " + short_url)
```

## Code. 
![Code](https://tinyurl.com/284m29g9?raw=true) 
