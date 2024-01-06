class User:
    def __init__(self, username, password):
        self.username = username
        self.email = (username + '@magoo.com').lower()
        self.password = password
        self.posts = []

class Post:
    def __init__(self, title, body, author):
        self.title = title
        self.body = body
        self.author = author
        self.author.posts.append(self)
    
    def publish(self):
        print(f'{self.title}\n {self.body} \n Connect with me at {self.author.email}')

gvj = User('GVJuan', 'pass123')

new_post = Post('Bad weather day', "I can't believe how rough the weather has been this year!", gvj)

for p in gvj.posts:
    p.publish()