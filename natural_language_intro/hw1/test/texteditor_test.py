import pytest


@pytest.mark.parametrize('data, expected',
    [('aaAaa','aaaaa')
    ])
def test_transform(data, expected):
    from hw1.texteditor import TextTransformer, TextEditor
    editor = TextEditor()
    target = TextTransformer([
        editor.to_lower
    ])
    assert target.transform(data) == expected

@pytest.mark.parametrize('data, expected',
    [('&copy; 2013','© 2013'),
     ('&quot;','"'),
     ('&apos;',"'")
    ])
def test_convert_html_symbol(data, expected):
    from hw1.texteditor import TextEditor
    target = TextEditor()
    assert target.convert_html_symbol(data) == expected

@pytest.mark.parametrize('data, expected',
    [('@user aaaa','aaaa'),
     ('aa1 @user aa1 aa1','aa1 aa1 aa1'),
     ('1aa @user', '1aa')
    ])
def test_remove_at_word(data, expected):
    from hw1.texteditor import TextEditor
    target = TextEditor()
    assert target.remove_at_word(data) == expected

@pytest.mark.parametrize('data, expected',
    [("can't",'cannot'),
     ("didn't",'did not'),
     ("aaa'aa", "aaa'aa")
    ])
def test_change_apostrophe_word(data, expected):
    from hw1.texteditor import TextEditor
    target = TextEditor()
    assert target.change_apostrophe_word(data) == expected

@pytest.mark.parametrize('data, expected',
    [("afk",'away from keyboard'),
     ("aaa", 'aaa')
    ])
def test_change_abbreviation_to_words(data, expected):
    from hw1.texteditor import TextEditor
    target = TextEditor()
    assert target.change_abbreviation_to_words(data) == expected

@pytest.mark.parametrize('data, expected',
    [(":‑)", 'happy'),
     (":-(", 'sad'),
     ("aaa", 'aaa')
    ])
def test_change_emoticon_to_word(data, expected):
    from hw1.texteditor import TextEditor
    target = TextEditor()
    assert target.change_emoticon_to_word(data) == expected

@pytest.mark.parametrize('data, expected',
    [("aa, aa", 'aa  aa'),
    ])
def test_remove_punctuation(data, expected):
    from hw1.texteditor import TextEditor
    target = TextEditor()
    assert target.remove_punctuation(data) == expected

@pytest.mark.parametrize('data, expected',
    [("aa$ aa", 'aa  aa'),
    ])
def test_remove_spec_symbol(data, expected):
    from hw1.texteditor import TextEditor
    target = TextEditor()
    assert target.remove_spec_symbol(data) == expected

@pytest.mark.parametrize('data, expected',
    [("aa123 aa", 'aa    aa'),
    ])
def test_remove_spec_symbol(data, expected):
    from hw1.texteditor import TextEditor
    target = TextEditor()
    assert target.remove_numbers(data) == expected

@pytest.mark.parametrize('data, expected',
    [("aa123 a aa", 'aa123 aa'),
    ])
def test_remove_word_with_len_one(data, expected):
    from hw1.texteditor import TextEditor
    target = TextEditor()
    assert target.remove_word_with_len_one(data) == expected