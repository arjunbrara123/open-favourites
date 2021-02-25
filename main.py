import webbrowser

url1 = 'http://docs.python.org/'
url2 = 'http://google.com/'

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

webbrowser.get(chrome_path).open(url1)
webbrowser.get(chrome_path).open(url2)
