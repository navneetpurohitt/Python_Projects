class User:
    def __init__(self, username):
        self.username = username
        self.posts = []
        self.followers = []

    def create_post(self, content):
        post = Post(content, self)
        self.posts.append(post)
        return post

    def follow(self, other_user):
        if other_user not in self.followers:
            self.followers.append(other_user)

    def __str__(self):
        return f"User: {self.username}, Followers: {len(self.followers)}, Posts: {len(self.posts)}"


class Post:
    def __init__(self, content, user):
        self.content = content
        self.likes = 0
        self.comments = []
        self.user = user  # Aggregation: Post is associated with a User

    def add_comment(self, comment_content, user):
        comment = Comment(comment_content, self, user)
        self.comments.append(comment)
        return comment

    def like_post(self):
        self.likes += 1

    def __str__(self):
        return f"Post: {self.content}, Likes: {self.likes}, Comments: {len(self.comments)}"


class Comment:
    def __init__(self, content, post, user):
        self.content = content
        self.post = post  # Aggregation: Comment is associated with a Post
        self.user = user  # Aggregation: Comment is associated with a User

    def __str__(self):
        return f"Comment by {self.user.username}: {self.content}"


# Example usage
if __name__ == "__main__":
    try:
        user1 = User("Alice")
        user2 = User("Bob")

        user1.follow(user2)
        print(user1)

        post1 = user1.create_post("Hello, world!")
        print(post1)

        post1.like_post()
        print(post1)

        comment1 = post1.add_comment("Nice post!", user2)
        print(comment1)

    except Exception as e:
        print(f"An error occurred: {e}")