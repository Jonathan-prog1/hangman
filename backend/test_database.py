from database import Database

def test_add_word(mocker):
    mock_conn = mocker.patch("sqlite3.connect")
    mock_cusor = mock_conn.return_value.cursor.return_value
    db = Database()
    db.add_one("hi")
    mock_conn.assert_called_once_with("backend/wordlist.db")
    mock_cusor.execute.assert_called_once_with(
        "INSERT INTO words VALUES (?)", ("hi",)
    )

def test_add_sample(mocker):
    mock_conn = mocker.patch("sqlite3.connect")
    mock_cusor = mock_conn.return_value.cursor.return_value
    db = Database()
    db.add_sample(["hi","bye"])
    mock_conn.assert_called_once_with("backend/wordlist.db")
    mock_cusor.executemany.assert_called_once_with(
        "INSERT INTO words VALUES (?)", ["hi","bye"]
    )

def test_add_showall(mocker):
    mock_conn = mocker.patch("sqlite3.connect")
    mock_cusor = mock_conn.return_value.cursor.return_value
    db = Database()
    db.showall()
    mock_conn.assert_called_once_with("backend/wordlist.db")
    mock_cusor.execute.assert_called_once_with(
        "SELECT rowid, * FROM words"
    )

def test_all_words(mocker):
    mock_conn = mocker.patch("sqlite3.connect")
    mock_cusor = mock_conn.return_value.cursor.return_value
    db = Database()
    db.all_words()
    mock_conn.assert_called_once_with("backend/wordlist.db")
    mock_cusor.execute.assert_called_once_with(
        "SELECT name FROM words"
    )

def test_delete_one(mocker):
    mock_conn = mocker.patch("sqlite3.connect")
    mock_cusor = mock_conn.return_value.cursor.return_value
    db = Database()
    db.delete_one("1")
    mock_conn.assert_called_once_with("backend/wordlist.db")
    mock_cusor.execute.assert_called_once_with(
        "DELETE FROM words WHERE rowid = (?)", ("1",) 
    )

def test_delete_one(mocker):
    mock_conn = mocker.patch("sqlite3.connect")
    mock_cusor = mock_conn.return_value.cursor.return_value
    db = Database()
    db.update_word("hi", "1")
    mock_conn.assert_called_once_with("backend/wordlist.db")
    mock_cusor.execute.assert_called_once_with(
        "UPDATE words SET name = ? WHERE rowid = ? ", ("hi", "1")
    )

def test_delete_one(mocker):
    mock_conn = mocker.patch("sqlite3.connect")
    mock_cusor = mock_conn.return_value.cursor.return_value
    db = Database()
    db.one_word("1")
    mock_conn.assert_called_once_with("backend/wordlist.db")
    mock_cusor.execute.assert_called_once_with(
        "SELECT * FROM words WHERE rowid = (?)",("1",)
    )