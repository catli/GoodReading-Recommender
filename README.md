#### GoodReading Recommender


The goal of this project is to build a recommender system for books
using good reads data, from this ![source](https://www.kaggle.com/philippsp/book-recommender-collaborative-filtering-shiny/data). Below is the description of each dataset available (from the site):


`ratings.csv`: contains ratings and looks like that:

```
book_id,user_id,rating
1,314,5
1,439,3
1,588,5
1,1169,4
1,1185,4
```


`to_read.csv`: provides IDs of the books marked "to read" by each user, as user_id,book_id pairs.

`books.csv`: metadata for each book (goodreads IDs, authors, title, average rating, etc.).

The metadata have been extracted from goodreads XML files, available in the third version of this dataset as books_xml.tar.gz. The archive contains 10000 XML files. One of them is available as sample_book.xml. To make the download smaller, these files are absent from the current version. Download version 3 if you want them.

`book_tags.csv`: tags/shelves/genres assigned by users to books. Tags in this file are represented by their IDs.

`tags.csv`: translates tag IDs to names.


