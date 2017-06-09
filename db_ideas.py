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

def saveIdea(user_name = '',idea_id = '',title = '',contents = '',comments = '',direction = None,score = None):
    if(not idea_id):
        return False
    return Ideas.create(user_name = user_name,idea_id = idea_id,title = title,contents = contents, comments = comments, direction = direction,score = score)

def saveIdeaWithCheck( user_name = '',idea_id = '',title = '',contents = '',comments = '',direction = None,score = None ):
    if(not idea_id):
        return False
    sqlIns = Ideas.select(Ideas,fn.Count(Ideas.id).alias('count')).where(Ideas.idea_id == idea_id)
    count = sqlIns.get().count
    if(count > 0):
        for item in sqlIns:
            updateIdeas(user_name = user_name,idea_id = idea_id,title = title,contents = contents, comments = comments, direction = direction,score = score,executeIns = item)
    else:
        saveIdea(user_name = user_name,idea_id = idea_id,title = title,contents = contents, comments = comments, direction = direction,score = score)

def updateIdeas(user_name = '',idea_id = '',title = '',contents = '',comments = '',direction = None,score = None ,executeIns = None):
    if(executeIns):
        executeIns.contents = contents
        executeIns.comments = comments
        executeIns.direction = direction
        executeIns.score = score
        executeIns.save()
    else:
        if(not idea_id):
            return False
        Ideas.update(user_name = user_name,title = title,contents = contents, comments = comments, direction = direction,score = score).where(idea_id == idea_id).execute()

def getIdeas(pageNum = 1,pageSize = 20):
    return Ideas.select().paginate(pageNum,paginate_by = pageSize).execute()
    
if __name__ == '__main__':
    saveIdeaWithCheck(idea_id = '?',contents = 'hhhhhh')
    