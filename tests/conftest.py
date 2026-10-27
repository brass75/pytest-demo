from pathlib import Path
from tempfile import TemporaryDirectory
import pytest


@pytest.fixture(scope="function")
def temp_dir() -> Path:
    with TemporaryDirectory() as tmp_dir:
        yield Path(str(tmp_dir))


@pytest.fixture(scope="function", autouse=True)
def init_and_teardown():
    print("Starting up...")
    yield None
    print("Tearing down")
