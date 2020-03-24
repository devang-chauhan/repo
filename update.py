"""This script takes add extra element to the HTML file to update the webpage"""
r = open("test.html", "w+")
if r.mode == "r":
    fl = r.readlines()
    for x in fl:
        print x
    for i in range(10):
        r.write("This is line number {} \r\n".format(i))
r.close()
