cache = {}

# links = [f"https://jsonplaceholder.typicode.com/comments/{id_}" for id_ in range(1, 100)]
links = [(f"https://jsonplaceholder.typicode.com/comments/{id_}", id_) for id_ in range(1, 100)]

links1 = ["http://127.0.0.1:5000/",
        "http://127.0.0.1:5000/a",
        "http://127.0.0.1:5000/b",
        "http://127.0.0.1:5000/c",
        "http://127.0.0.1:5000/d",
        ]

link = ["http://127.0.0.1:5000/"]

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]
