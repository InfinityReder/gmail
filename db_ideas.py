from peewee import *

DATABASE = 'test.db'
DEBUG = True
SECRET_KEY = ''

db = SqliteDatabase(DATABASE)

class BaseModel(Model):
    class Meta:
        database = db

class Ideas(BaseModel):
    user_name = CharField()
    idea_id = CharField()
    title = CharField()
    contents = BlobField()
    comments = BlobField()
    direction = IntegerField()
    score = IntegerField()

# def saveIdea(user_name = '',idea_id = '',title = '',contents = '',contents = '',comments = '',direction = None,score = None):
#     return Ideas.create(user_name = user_name,idea_id = idea_id,title = title,contents = contents, comments = comments, direction = direction,score = score)

def getIdeas(pageNum = 1,pageSize = 20):
    return Ideas.select().paginate(pageNum,paginate_by = pageSize).get()
    
