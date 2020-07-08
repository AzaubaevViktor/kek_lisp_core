import pytest


@pytest.mark.parametrize('app_name', app_names)
def test_app(test_executor, app_name):
    try:
        test_executor.run_source(ModuleSource(app_name))
        assert 'bad' not in app_name
    except AssertionError as e:
        assert 'bad' in app_name, e
