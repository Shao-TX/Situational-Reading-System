import json

with open('books.json') as f:
    data = json.load(f)
    img = data['page1']['image']
    music = data['page1']['music']
    device = data['page1']['device']

print(img)
print(music)
print(device[0])