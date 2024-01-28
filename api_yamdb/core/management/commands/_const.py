DATA_REVIEWS_APP = [
    [
        'reviews',
        'Categories',
        'data/category.csv',
    ],
    [
        'titles',
        'Genres',
        'data/genre.csv'
    ],
    [
        'titles',
        'TitlesModel',
        'data/titles.csv',
        ['category'],
    ],
    [
        'reviews',
        'TitlesGenres',
        'data/genre_title.csv',
        ['title', 'genre'],
    ],
    [
        'reviews',
        'Review',
        'data/review.csv',
        ['title_id', 'author'],
    ],
    [
        'reviews',
        'Comment',
        'data/comments.csv',
        ['review_id', 'author'],
    ],
]

DATA_USER_APP = [
    ['users', 'User', 'data/users.csv'],
]
