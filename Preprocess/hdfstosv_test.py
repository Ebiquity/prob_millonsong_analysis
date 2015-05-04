from hdftotsv import *
from mock import mock_open, patch, call


def test_correctly_get_file_from_single_dir():
    files = discover_files("../data/subset/cvt_extraction")
    assert len(files) == 15
    assert files[0] == "TRADTAV128F14B0F47.h5"
    assert files[9] == "TRADTQK12903CB67C9.h5"


def test_correctly_extract_song_info():
    filename = "../data/subset/cvt_extraction/TRADTAV128F14B0F47.h5"

    song_data_rows = get_song_data_rows(filename)

    assert len(song_data_rows) == 1
    assert len(song_data_rows[0]) == 20


def test_correctly_extract_song_metadata():
    tol = 0.01

    filename = "../data/subset/cvt_extraction/TRADTAV128F14B0F47.h5"

    song_data_rows = get_song_data_rows(filename)
    row = song_data_rows[0]

    assert abs(row[2] - 0.7) < tol
    assert abs(row[3] - 0.52) < tol
    assert row[4] == 'ARJ7SQ31187B9AF432'  # Artist ID
    assert row[9] == 'Billy Bragg & Wilco'  # Artist name
    assert row[18] == 'She Came Along To Me (LP Version)'  # Title
    assert row[17] == 'SOSIMGO12A6D4FB491'  # SongID


def test_write_artist_table_single_row():
    m = mock_open()
    data = [('1', 2, '3', '4')]

    expected_calls = [call('artist_data.tsv', 'a'),
                      call().__enter__(),
                      call().write('1\t2\t3\t4'),
                      call().write('\n'),
                      call().__exit__(None, None, None)]

    with patch('hdftotsv.open', m, create=True):
        append_artist_data(data)

    assert expected_calls == m.mock_calls


def test_enumerate_input_files():
    files = discover_files("../data/subset/cvt_large_test/")
    assert len(files) == 553
    assert files[0] == "data/A/D/A/TRADABC128F4274FCC.h5"
    assert files[19] == "data/A/D/B/TRADBSW128F933A7A8.h5"
    assert files[290] == "data/A/D/Y/TRADYZC12903CCC8FA.h5"
    assert files[545] == "data/B/E/Z/TRBEZFS128F92E40DD.h5"

