while True:
    import api_sr_GET_amd64 as bugslib
    import intapi_CONVERT_TO_HTML as icth
    try:
        aurl = input("URL: ")
        back = bugslib.api_getses(aurl)
        print(back)
        if "<html" in back:
            print("Detected html file!Do you want to convert it to html file?(y/n)")
            yon = input(">> ")
            if yon == "y":
                name = input("Save as: ")
                print("Converting...")
                icth.convert(back, name)
                print("Done!")
            else:
                print("Abort.")
    except TypeError:
        pass
    print("\n")


