from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

likes = db.Table(
    'likes',
    db.Model.metadata,
    db.Column('posts', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column('users', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)

class Post(db.Model):
    __tablename__= "posts"
    id = db.Column(db.Integer, primary_key= True)
    # erased unique = true on post_url
    post_url = db.Column(db.String, nullable= False)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    city = db.Column(db.String)
    state = db.Column(db.String)
    country = db.Column(db.String)
    caption = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    #relationships
    user = db.relationship("User", back_populates="posts")
    comments = db.relationship("Comment", back_populates="post")
    post_likes = db.relationship("User", back_populates="user_likes", secondary=likes, cascade="all, delete")

    def to_dict(self):
        return {
            "id": self.id,
            "postUrl": self.post_url,
            "ownerId": self.owner_id,
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "caption": self.caption,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "numLikes": len(self.post_likes),
            # added here
            # "user": str(self.user.username),
            "user": self.convert_user_to_dict(),
            "comments": [comment.to_dict() for comment in self.comments]
        }
    # added here
    def convert_user_to_dict(self):
        return {
            'id': self.user.id,
            'username': self.user.username,
            "firstName": self.user.first_name,
            "lastName": self.user.last_name,
            "profilePicUrl": self.user.profile_pic_url
        }


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key= True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    content = db.Column(db.String(250), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    #Relationships
    post = db.relationship("Post", back_populates="comments")
    user = db.relationship("User", back_populates="comments")

    def to_dict(self):
        return {
            "id": self.id,
            "postId": self.post_id,
            "userId": self.user_id,
            "content": self.content,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }


# class Like(db.Model):
#     __tablename__ = "likes"
#     id = db.Column(db.Integer, primary_key= True)
#     post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

#     #Relationships
#     post = db.relationship("Post", back_populates("likes"))


#     def to_dict(self):
#         return {
#             "postId" = self.post_id,
#             "userId" = self.user_id,
#         }


# class Following(db.Model):
#     __tablename__ = "followings"
#     user_following = db.Column(db.Integer, nullable=False )
#     user_followers = db.Column(db.Integer, nullable=False)
