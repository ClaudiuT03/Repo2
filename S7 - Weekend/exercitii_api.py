"""
HTTP. Rest APIs. Requests

Folosim https://jsonplaceholder.typicode.com/guide/
Toate requesturile se vor face prima data in Postman (pentru verificare),
iar apoi folosind libraria requests din Python.

Structura datelor este următoarea:
- fiecare post este deținut de un user, și poate avea mai multe comments
- fiecare album este deținut de un user, și poate avea mai multe photos
- fiecare todo este detinut de un user.

1. Alege un user din lista de useri predefiniti.
Pentru acesta, fa requesturile necesare pentru a afișa următoarele informații:
-> lista de posts
-> lista de albume
-> lista de todos
Pentru a menține output-ul la un nivel acceptabil, afișează la fiecare dintre aceste liste
doar informații despre primele 3 obiecte,
iar apoi afiseaza "+x more posts/albums/todos", unde x este numărul de obiecte rămase.
"""
import requests
# 1. Luam toate postarile pentru utilizatorul/user-ul cu id-ul 1
response = requests.get(url="https://jsonplaceholder.typicode.com/users/1/posts")

# informatii status code
# print(response.status_code)

# informatii continut raspuns

# 1. sub forma de bytes
# print(response.content)

# 2. sub forma de text
# print(response.text)

# 3. sub forma de json
posts = response.json()
print(posts)
# print(type(posts))
# print(posts[0])

# v1
for i in range(0, 3):
    post = posts[i]
    print(f"Post id {post['id']}, title {post['title']}, userId {post['userId']}")
left_posts = len(posts) - 3
print(f"+{left_posts} more posts")

# v2
# for post in posts[0:3]:
#     print(f"Post id {post['id']}, title {post['title']}, userId {post['userId']}")
# left_posts = len(posts) - 3
# print(f"+{left_posts} more posts")


# # v3
# for index, post in enumerate(posts):
#     if index > 2:
#         left_posts = len(posts) - 3
#         print(f"+{left_posts} more posts")
#         break
#     print(f"Post id {post['id']}, title {post['title']}, userId {post['userId']}")

"""
2. Alege un post, și afișează lista de comentarii.
Alege un album, si afiseaza lista de photos.
"""

"""
3. Creeaza un post nou (atentie, acesta NU va fi salvat, dar putem analiza răspunsul pentru a vedea cum ar arata
în viitor dacă ar fi fost salvat). Încearcă să-l creezi cu si fără id. Ce observi?
"""

"""
4. Alege un post existent și realizează operațiunile de PUT si PATCH
(atentie, modificările NU vor fi salvate, analizăm doar răspunsul).
Ce observi ca este diferit între cele 2 metode?
"""

"""
5. Folosind query parameters, filtrează lista de todos pentru userul ales astfel incat
sa afisezi doar todos care nu sunt completed.
"""

"""
6. Alege un album, și ia pozele din acesta în 2 moduri diferite (o data cu nested resource, o data folosind query params)
Verifica dacă exista vreo diferenta intre cele 2 rezultate.
"""
