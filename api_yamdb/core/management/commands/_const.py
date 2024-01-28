DATA_TITLES_APP = [
    [
        'titles',
        'CategoriesModel',
        'data/category.csv',
    ],
    ['titles', 'GenresModel', 'data/genre.csv'],
    [
        'titles',
        'TitlesModel',
        'data/titles.csv',
        ['category'],
    ],
    [
        'titles',
        'TitlesGenresModel',
        'data/genre_title.csv',
        ['title', 'genre'],
    ],
]
DATA_COMMENTS_APP = [
    [
        'comments',
        'ReviewModel',
        'data/review.csv',
        ['title_id', 'author'],
    ],
    [
        'comments',
        'CommentModel',
        'data/comments.csv',
        ['review_id', 'author'],
    ],
]
DATA_USER_APP = [
    ['users', 'User', 'data/users.csv'],
]
