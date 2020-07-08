import pytest


@pytest.mark.parametrize('file_name', file_names)
def test_test(test_executor, file_name):
    try:
        test_executor.run_source(FileSource(file_name))
        assert 'bad' not in file_name
    except AssertionError as e:
        assert 'bad' in file_name, e
