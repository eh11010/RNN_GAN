import facebook

graph = facebook.GraphAPI('EAAWuzhcPn9IBAPKDvaU0UP77Wj7sa9vwZC6wsNpjqZAagZBx99EI7OAea5bOFc3FYNIHgLcUEmsshawINSaEZAoN4StK0gdctzKyZA6xDzDKJkqKeLcuT7ZAMDIZAxaZAWm1r9YZBRwUyqVZCaIqTN0PZBi1UiWF8SPGKUQvfZCHuTt1iTpdZAZBhMOkr25leE2qXNsr2jbiRuh1RFUgZDZD')
graph.get_object("1599575056949202", "feed", message = "test!!")
