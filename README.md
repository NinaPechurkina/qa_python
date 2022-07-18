# qa_python

метод добавления книг и выставления книг по умолчанию add_new_book: 
- def test_add_new_book_add_rating_1

метод установления рейтинга книге set_book_rating:
- def test_add_new_book_no_rating_no_book
- test_add_new_book_rating_0
- test_add_new_book_rating_over_10
- test_add_new_book_no_rating

метод получения рейтинга книги по ее имени get_book_rating:
- test_add_new_book_set_book_rating

метод выведения списка книг с определенным рейтингом get_books_with_specific_rating:
- test_add_new_book_list_of_books_with_a_certain_rating

мтод получения словаря books_rating get_books_rating:
- def test_add_new_book_add_two_books
- test_add_new_book_add_identical_books_error

метод добавления книги в Избранное add_book_in_favorites:
- def test_add_new_book_add_to_favorites
- test_add_new_book_add_to_favorites_no_doubles

метод удаления книги из Избранного delete_book_from_favorites:
- test_add_new_book_delete_book_from_favorites

метод получения списка Избранных книг get_list_of_favorites_books:
- def test_add_new_book_add_to_favorites
- test_add_new_book_add_to_favorites_no_doubles
- test_add_new_book_no_add_to_favorites
- test_add_new_book_delete_book_from_favorites

