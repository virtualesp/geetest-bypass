from pathlib import Path

import pytest


@pytest.fixture
def cid() -> str:
    return '54088bb07d2df3c46b79f80300b0abbe'


@pytest.fixture
def out_dir():
    path = Path(__file__).resolve().parents[1] / 'resources'
    path.mkdir(parents=True, exist_ok=True)
    return path


@pytest.fixture
def svg_out_dir(out_dir):
    path = out_dir / 'svg'
    path.mkdir(parents=True, exist_ok=True)
    return path
