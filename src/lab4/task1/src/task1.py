class MovieLibrary:
    """Класс для списка фильмов"""
    def __init__(self, films_file):
        self.films_file = films_file
        self.films = {}

    def load_movies(self):
        """Список фильмов"""
        with open(self.films_file, 'r') as file:
            for line in file:
                film_id, title = line.strip().split(",", 1)
                self.films[int(film_id)] = title

    def get_movie_title(self, film_id):
        """Название фильма по его номеру"""
        return self.films.get(film_id, "Неизвестный фильм")


class WatchHistory:
    """Класс для истории просмотров"""
    def __init__(self, history_file):
        self.history_file = history_file
        self.history = []

    def load_history(self):
        """Список просмотров"""
        with open(self.history_file, 'r') as file:
            for line in file:
                self.history.append(list(map(int, line.strip().split(','))))


class MovieRecommender:
    """Класс для создания рекомендаций"""
    def __init__(self, films_library, watch_history):
        self.films_library = films_library
        self.watch_history = watch_history

    def recommend(self, user_watchlist):
        """Рекомендует фильм"""
        if not user_watchlist:
            return "Нет подходящих фильмов"

        # ищем пользователей с кем совпали просмотры
        similar_users = []
        for history in self.watch_history.history:
            common_films = [films for films in user_watchlist if films in history]
            if len(common_films) >= len(user_watchlist) / 2:
                similar_users.append(history)

        # убираем фильмы, которые уже смотрели
        all_recommended_movies = []
        for history in similar_users:
            all_recommended_movies.extend([movie for movie in history if movie not in user_watchlist])
        if not all_recommended_movies:
            return "Нет подходящих фильмов"

        # ищем самый популярный фильм
        films_counts = {}
        for movie in all_recommended_movies:
            if movie in films_counts:
                films_counts[movie] += 1
            else:
                films_counts[movie] = 1
        most_watched_film = max(films_counts, key=films_counts.get)
        return self.films_library.get_movie_title(most_watched_film)


def task1():
    """Функция для выполнения задачи"""
    FILM_FILE = "../files/films.txt"
    HISTORY_FILE = "../files/history.txt"
    INPUT_FILE = "../files/input.txt"

    films_library = MovieLibrary(FILM_FILE)
    films_library.load_movies()

    watch_history = WatchHistory(HISTORY_FILE)
    watch_history.load_history()

    with open(INPUT_FILE, 'r') as file:
        user_watchlist = list(map(int, file.readline().strip().split(',')))

    recommender = MovieRecommender(films_library, watch_history)
    recommendation = recommender.recommend(user_watchlist)

    print(f"Рекомендуем посмотреть: {recommendation}")


if __name__ == "__main__":
    task1()
