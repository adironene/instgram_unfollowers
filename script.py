fin = open('connections/followers_and_following/followers_1.html')
data = fin.readlines()
parsed = data[0].split('instagram.com/')
parsed_followers = [s.split("\">")[0] for s in parsed]

fin = open('connections/followers_and_following/following.html')
data = fin.readlines()
parsed = data[0].split('instagram.com/')
parsed_following = [s.split("\">")[0] for s in parsed]

hashed_followers = {}
hashed_following = {}

for follower in parsed_followers:
    hashed_followers[follower] = 0

for following in hashed_following:
    hashed_following[following] = 0
    
fakes = []
fans = []

for following in parsed_following:
    if following not in hashed_followers:
        fakes.append(following)
        
for follower in parsed_followers:
    if follower not in hashed_following:
        fans.append(follower)
        
print("people that don't follow you back:")
for fake in fakes: print(fake)