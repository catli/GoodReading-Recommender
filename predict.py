import pandas as pd
import numpy as np
import seaborn as sns
from surprise import Dataset, Reader, NMF, SVD, KNNBasic, accuracy
from surprise.model_selection import cross_validate, train_test_split
import matplotlib.pyplot as plt
import pdb



class BookRecommender:

    def __init__(self, data, model):
        self.data = data
        self.model = model

    def fitTrainData(self):
        self.filterData()
        self.loadReaderformat()
        self.splitTrainTest()
        self.model.fit(self.train_data)

    def filterData(self, threshold = 2):
        # use a threshold count to filter out without minimum numbre of ratings
        data_grouped = self.data.groupby(
            ['user_id']).count()['rating'].reset_index()
        users = data_grouped[data_grouped.rating>threshold].user_id
        self.new_data = self.data[self.data.user_id.isin(users)]

    def loadReaderformat(self):
        reader = Reader(rating_scale = (1,5))
        self.reader_data = Dataset.load_from_df(
            self.new_data[['user_id', 'book_id', 'rating']], reader)

    def splitTrainTest(self, test_size = 0.2):
        self.train_data, self.test_data = train_test_split(
            self.reader_data, test_size = test_size)

    def evaluate(self, data):
        predictions = self.genMissingPredictions(data)
        topn = self.getTopNPredictions(predictions)
        return top_n

    def genMissingPredictions(self, data):
        testset = data.build_anti_testset()
        predictions = self.model.test(testset)
        return predictions

    def getTopNPredictions(self, predictions, n = 10):
        top_n = {}
        for user_id, book_id, true_r, est, _ in predictions:
            top_n[user_id] = top_n.get(user_id, []).append((book_id, est))
        for user_id, user_ratings in top_n.items():
            # sort by estimate
            user_ratings.sort(key = lambda x: x[1], reverse= True)
            top_n[user_id] = user_ratings[:n]
        return top_n



if __name__ == '__main__':
    ratings = pd.read_csv('/Users/cathleen/Documents/goodreads_data/ratings.csv')
    books = pd.read_csv('/Users/cathleen/Documents/goodreads_data/books.csv')
    print('Read csv')
    algo = SVD()
    print('Recommender')
    recommender = BookRecommender(ratings, algo)
    print('fit model')
    recommender.fitTrainData()
    print('predictions')
    top_n = recommender.evaluate(recommender.train_data)
