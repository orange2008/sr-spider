while True:
	import api_sr_GET_amd64 as bugslib
	aurl = input("URL: ")
	back = bugslib.api_getses(aurl)
	print(back)
	print("\n")

