import search

def test_count_in_python_site():
    count = search.wordCount("https://python.org/", "python")
    assert count == 25
