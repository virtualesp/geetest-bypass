# wulu-geetest-bypass-voice

Voice solver for [wulu-geetest-bypass](https://github.com/wulu007/geetest-bypass).

> **Note**: This is an extension package for `wulu-geetest-bypass` and is not intended for standalone use. Install via the main package instead.

Provides the full offline voice digit recognition engine (MFCC + pre-computed centroids for 12 languages), enabling Geetest v4 voice captchas to be solved without any deep learning framework.

## Installation

```bash
pip install wulu-geetest-bypass[voice]
```

## Plugin registration

This package registers its solver with the main package via the
`wulu_geetest_bypass.solvers` entry point group, so voice captchas are
handled automatically once the package is installed.

Third-party packages wanting to replace this engine can register their own
`voice` entry point in the same group, or use `Geetest.register_solver('voice', my_func)`
at runtime.

## Supported Languages

| Code | Language |
|------|----------|
| ara | Arabic |
| deu | German |
| eng | English |
| fra | French |
| ind | Indonesian |
| jpn | Japanese |
| kor | Korean |
| por | Portuguese |
| rus | Russian |
| spa | Spanish |
| zho | Chinese (Mandarin) |
| zho-hk | Chinese (Cantonese) |

## Usage

```python
from wulu_geetest_bypass import Geetest

g = Geetest(captcha_id='...', risk_type='voice')
seccode = await g.resolve()
```
