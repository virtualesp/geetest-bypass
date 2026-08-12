import numpy as np
from wulu_geetest_bypass_voice.solver import _split_by_silence


def test_split_by_silence_empty():
    assert _split_by_silence(np.array([], dtype=np.float32), 16000) == []


def test_split_by_silence_single_segment():
    sr = 16000
    y = np.concatenate(
        [
            np.zeros(sr // 2, dtype=np.float32),
            np.ones(sr, dtype=np.float32) * 0.5,
            np.zeros(sr // 2, dtype=np.float32),
        ]
    )
    segs = _split_by_silence(y, sr)
    assert len(segs) == 1
    assert len(segs[0]) >= sr


def test_split_by_silence_merges_nearby_segments():
    sr = 16000
    short_gap = int(sr * 0.1)
    y = np.concatenate(
        [
            np.ones(sr // 2, dtype=np.float32) * 0.5,
            np.zeros(short_gap, dtype=np.float32),
            np.ones(sr // 2, dtype=np.float32) * 0.5,
        ]
    )
    segs = _split_by_silence(y, sr)
    assert len(segs) == 1
