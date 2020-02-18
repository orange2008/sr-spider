# api syntax: 
# url = input("URL: ")
# from api_sr_GET_amd64 import api_getses
# result = api_getses(url)
# print(result)
# --------or--------
# print(api_getses(url)

# DON'T USE api_getses(url)!!! BECAUSE WE USE 'return'.
def api_getses(url):
    try:
        import requests
    except ImportError:
        print("Requests didn't install, installing...")
        os.system("pip install requests")
        import requests
    
    print("Downloading...")
    raw = requests.get(url)
    status_code = raw.status_code
    text = raw.text
    print("What do you want to do?")
    print("1. Get raw data.")
    print("2. Get status code.")
    print("3. Get text inside.")
    opt = input(">> ")
    if opt == "1":
        print("Ok.")
        return raw
    elif opt == "2":
        print("Ok.")
        return status_code
    elif opt == "3":
        print("Ok.")
        return text
    else:
        print("Not detected, returning raw footage...")
        return raw