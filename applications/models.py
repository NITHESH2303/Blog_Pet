

class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # __repr__ --> representation of object
    def __repr__(self):
        return 'Blog post' + str(self.id)