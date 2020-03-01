import requests
import ctypes

url = "https://picsum.photos/4096/2160/"

response = requests.get(url)
if response.status_code == 200:
    print("Page opened, succesfully, downloading image...")
    with open('C:/Users/Dogukan/Pictures/Saved Pictures/new_wallpaper.jpg','wb') as file:
        file.write(response.content)
else:
    print("request could not be opened, error code " + str(response.status_code))

print("Retrieving HTTP meta-data...")
print(response.status_code)
print(response.headers['content-type'])
print(response.encoding)

ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/Dogukan/Pictures/Saved Pictures/new_wallpaper.jpg" , 0)

