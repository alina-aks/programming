import unittest
import datetime
from time import perf_counter
from src.lab4.task1.src.task1 import MovieLibrary, WatchHistory, MovieRecommender

class TestMovieRecommender(unittest.TestCase):

    def setUp(self):
        self.film_file = "../../src/lab4/task1/files/films.txt"
        self.history_file = "../../src/lab4/task1/files/history.txt"

        self.library = MovieLibrary(self.film_file)
        self.library.load_movies()

        self.history = WatchHistory(self.history_file)
        self.history.load_history()

        self.recommender = MovieRecommender(self.library, self.history)

    def test_should_recommend_film_for_similar_list(self):
        #given
        user_watchlist = [2, 14]
        expected_result = "Форрест Гамп"
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = self.recommender.recommend(user_watchlist)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        #then
        self.assertEqual(result, expected_result, "Рекомендация не корректна.")
        self.assertLessEqual(result_time.total_seconds(), expected_time,f"Значение {result_time} превышает порог {expected_time}")

    def test_should_recommend_film_for_medium_list(self):
        #given
        user_watchlist = [1,2,19,39,45,47]
        expected_result = "Темный рыцарь"
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = self.recommender.recommend(user_watchlist)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        #then
        self.assertEqual(result, expected_result, "Рекомендация не корректна.")

    def test_should_not_recommend_film(self):
        #given
        user_watchlist = [2, 14, 26, 47, 13, 25]
        expected_result = "Нет подходящих фильмов"
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = self.recommender.recommend(user_watchlist)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        #then
        self.assertEqual(result, expected_result, "Рекомендация не корректна.")

    def test_no_common_films(self):
        #given
        user_watchlist = [51,59]
        expected_result = "Нет подходящих фильмов"
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = self.recommender.recommend(user_watchlist)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест4.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result, "Рекомендация не корректна.")

    def test_no_watched_films(self):
        #given
        user_watchlist = []
        expected_result = "Нет подходящих фильмов"
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = self.recommender.recommend(user_watchlist)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест5.Итоговое время алгоритма:", result_time)

        #then
        self.assertEqual(result, expected_result, "Рекомендация не корректна.")

    def test_should_recommend_film_for_list(self):
        #given
        user_watchlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        expected_result = "Дэдпул"
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = self.recommender.recommend(user_watchlist)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест6.Итоговое время алгоритма:", result_time)

        #then
        self.assertEqual(result, expected_result, "Рекомендация не корректна.")

if __name__ == "__main__":
    unittest.main()
