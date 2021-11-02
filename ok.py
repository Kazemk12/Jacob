import webbrowser

url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'


chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


webbrowser.get(chrome_path).open(url)