from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime


cluster = MongoClient(
    'mongodb+srv://mongo_maty:<password>@cluster0.irz1z.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = cluster['news']
collection = db['articles']

post = {
    'name': 'article',
    'title': 't 1',
    'tags': [
        'a',
        'b',
        'c'
    ],
    '_time': datetime.utcnow()
}
posts = [
    {
        'name': 'article',
        'title': 't 2',
        'tags': [
            'c',
            'd'
        ],
        '_time': datetime.utcnow()

    },
    {
        'name': 'article',
        'title': 't 3',
        'tags': [
            'b',
            'c',
            'd'
        ],
        '_time': datetime(2021, 7, 22, 20, 0, 0)
    }
]

collection.insert_one(post)  # insert one post
collection.insert_many(posts)  # insert a list of posts
result = collection.find_one(
    {
        'name': 'article',
        'tags': 'a'
    }
)  # retreive one post with specs
result2 = collection.find_one(
    {
        '_id': ObjectId('60f9aa29233fee868be2d738')
    }
)  # retreive one post by id
print(result)
print(result2)

results = collection.find(
    {
        'tags': 'b'
    }
)  # retreive all posts with specs in a cursor object (consumable)
print(results)
for res in results:  # iterate over the cursor to get the actuall items
    print(res)

# count posts with specs (empty for all)
print(collection.count_documents({'tags': 'a'}))

# find docs with range:
for a in collection.find({'_time': {'$gt': datetime(2021, 7, 22, 20, 30, 0)}}).sort('title'):
    print(f'found: {a}')

collection.delete_one(
    {
        '_id': ObjectId('60f9aa29233fee868be2d738')
    }
)  # delete one post by id
collection.delete_many(
    {
        'name': 'article'
    }
)  # delete many posts by specs

# count posts with specs (empty for all)
print(collection.count_documents({}))

# update posts:
collection.update_many(
    {},
    {'$set': {'_time': datetime.now()}}
)
