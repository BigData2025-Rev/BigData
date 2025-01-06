# Inserting values into a collection
db.movies.insertMany([
{
title : "Fight Club",
writer : "Chuck Palahniuk",
year : 1999,
actors : [
  "Brad Pitt",
  "Edward Norton"
]
},
{
title : "Pulp Fiction",
writer : "Quentin Tarantino",
year : 1994,
actors : [
  "John Travolta",
  "Uma Thurman"
]
},
{
title : "Inglorious Basterds",
writer : "Quentin Tarantino",
year : 2009,
actors : [
  "Brad Pitt",
  "Diane Kruger",
  "Eli Roth"
]
},
{
title : "The Hobbit: An Unexpected Journey",
writer : "J.R.R. Tolkein",
year : 2012,
franchise : "The Hobbit"
},
{
title : "The Hobbit: The Desolation of Smaug",
writer : "J.R.R. Tolkein",
year : 2013,
franchise : "The Hobbit"
}
]);

## Querying

1) get all documents
    - db.movies.find()

2) get all documents with writer set to "Quentin Tarantino"
    - db.movies.find({writer:"Quentin Tarantino"})

3) get all documents where actors include "Brad Pitt"
    - db.movies.find({actors:"Brad Pitt"})

4) get all documents with franchise set to "The Hobbit"
    - db.movies.find({franchise:"The Hobbit"})

5) get all movies released in the 90s
    - db.movies.find({year:{$gt: 1989, $lt: 2000}})
 
6) get all movies released before the year 2000 or after 2010
    - db.movies.find({$or: [{year: {$lt:2000}}, {year: {$gt:2010}}]})

## Updating

1) add a synopsis to "The Hobbit: An Unexpected Journey" : "A reluctant hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home - and the gold within it - from the dragon Smaug."
    - db.movies.updateOne({title: "The Hobbit: An Unexpected Journey"}, {$set: {synopsis:"A reluctant hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home - and the gold within it - from the dragon Smaug."}})

2) add a synopsis to "The Hobbit: The Desolation of Smaug" : "The dwarves, along with Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug. Bilbo Baggins is in possession of a mysterious and magical ring."
    - db.movies.updateOne({title:"The Hobbit: The Desolation of Smaug"}, {$set: {synopsis: "The dwarves, along with Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug. Bilbo Baggins is in possession of a mysterious and magical ring."}})

3) add an actor named "Samuel L. Jackson" to the movie "Pulp Fiction"
    - db.movies.updateOne({title:"Pulp Fiction"}, {$push: {actors: "Samuel L. Jackson"}})

## Text Search

1) find all movies that have a synopsis that contains the word "Bilbo"
    - db.movies.find({$text:{$search:"Bilbo"}})

2) find all movies that have a synopsis that contains the word "Gandalf"
    - db.movies.find({synopsis: /Gandalf/})

3) find all movies that have a synopsis that contains the word "Bilbo" and not the word "Gandalf"
    - db.movies.find({ synopsis: { $regex: '\\bBilbo\\b', $not:{$regex: '\\bGandalf\\b'}}})
    - db.movies.find({$text: {$search: "Bilbo -Gandalf"}})

4) find all movies that have a synopsis that contains the word "dwarves" or "hobbit"
    - db.movies.find({ $text: {$search: "dwarves hobbits"}})
    - db.movies.find({ synopsis: { $regex: "dwarves|hobbits"}})
    - db.movies.find({ synopsis: { $in : [/dwarves/, /hobbits/]}})

5) find all movies that have a synopsis that contains the word "gold" and "dragon"
    - db.movies.find({ synopsis: { $regex: '\\bgold\\b', $regex: '\\bdragon\\b'}})
    - db.movies.find({$text: {$search:"gold", $search:"dragon"}})

## Delete

1) delete the movie "Fight Club"
    - db.movies.deleteOne({title:"Fight Club"})

2) delete the movies where Quentin Tarantino is a writer
    - db.movies.deleteMany({writer: "Quentin Tarantino"})