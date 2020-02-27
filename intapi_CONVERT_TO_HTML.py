import os
import json
import time
def convert(needtoconvert, output):
    print("We will write this web page to " + output + ".html")
    print("Start in 3 secounds.")
    print("If you have a exist " + output + ".html file in this folder, we will overwrite it!")
    time.sleep(3)
    print("Beginning...")
    result = output + ".html"
    with open(result, 'w') as opt:
        opt.write(needtoconvert)
    print("Ok.")

