from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_rating_1(self):
        collector = BooksCollector()
        collector.add_new_book('Mur-mur')

        assert collector.get_book_rating('Mur-mur') == 1

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2


    def test_add_new_book_add_identical_books_error(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        books_rating = collector.get_books_rating()

        assert len(books_rating) == 1
        assert not len(collector.get_books_rating()) == 2

    def test_add_new_book_set_book_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Mur-mur')
        collector.set_book_rating('Mur-mur', 10)

        assert collector.get_book_rating('Mur-mur') == 10

    def test_add_new_book_no_rating_no_book(self):
        collector = BooksCollector()
        collector.set_book_rating('Mur-mur', 10)

        assert len(collector.get_books_rating()) == 0

    def test_add_new_book_rating_0(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 0)

        assert collector.books_rating.get('Гордость и предубеждение и зомби') == 1

    def test_add_new_book_rating_over_10(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 50)

        assert collector.books_rating.get('Гордость и предубеждение и зомби') == 1

    def test_add_new_book_list_of_books_with_a_certain_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        collector.add_new_book('Mur-mur')
        collector.set_book_rating('Mur-mur', 10)
        collector.add_new_book('My cat')
        collector.set_book_rating('My cat', 10)

        assert collector.get_books_with_specific_rating(10) == ['Mur-mur', 'My cat']

    def test_add_new_book_no_rating(self):
        collector = BooksCollector()
        collector.set_book_rating('Гордость и предубеждение и зомби', 2)

        assert collector.books_rating.get('Гордость и предубеждение и зомби') == None

    def test_add_new_book_add_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Mur-mur')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Mur-mur')

        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Mur-mur']

    def test_add_new_book_add_to_favorites_no_doubles(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Mur-mur')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Mur-mur')
        collector.add_book_in_favorites('Mur-mur')

        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Mur-mur']

    def test_add_new_book_no_add_to_favorites(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Mur-mur')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_new_book_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Mur-mur')
        collector.add_book_in_favorites('Mur-mur')
        collector.delete_book_from_favorites('Mur-mur')

        assert len(collector.get_list_of_favorites_books()) == 0
