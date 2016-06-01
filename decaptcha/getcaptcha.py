import urllib.request

for i in range(20):
    url = "http://scm.sf-express.com/isc-vmi/loginmgmt/imgcode?a=0.18090831750297091"
    resp = urllib.request.urlopen(url)
    content = resp.read()
    print("downloaded",i)

    with open("./captcha/%04d.jpeg"%i,"wb") as file:
        file.write(content)
        file.close()

