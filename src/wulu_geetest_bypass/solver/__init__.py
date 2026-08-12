import functools
import importlib
import importlib.metadata
from collections.abc import Callable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .match import solve_match
    from .slide import solve_slide
    from .svg import solve_svg
    from .voice import solve_voice
    from .winlinze import solve_winlinze


__all__ = [
    'discover_plugins',
    'solve_match',
    'solve_slide',
    'solve_svg',
    'solve_voice',
    'solve_winlinze',
]

_ENTRY_POINT_GROUP = 'wulu_geetest_bypass.solvers'


@functools.lru_cache(maxsize=1)
def discover_plugins() -> dict[str, Callable]:
    """Discover third-party solvers registered via entry points.

    Plugin packages register their solvers under the
    ``wulu_geetest_bypass.solvers`` entry point group, e.g.::

        [project.entry-points."wulu_geetest_bypass.solvers"]
        icon = "my_pkg.solver:solve_icon"

    The entry point *name* is the ``captcha_type`` it handles; the value is
    a ``module:attribute`` reference to the solver callable. The result is
    cached after the first call.
    """
    solvers: dict[str, Callable] = {}
    for ep in importlib.metadata.entry_points(group=_ENTRY_POINT_GROUP):
        try:
            solvers[ep.name] = ep.load()
        except Exception:
            continue
    return solvers


def __getattr__(name):
    if name in __all__:
        module_name = name.replace('solve_', '', 1)
        try:
            module = importlib.import_module(f'.{module_name}', package=__name__)
            return getattr(module, name)
        except ImportError as e:
            err = e

            def _missing_dependency_stub(*args, **kwargs):
                raise ImportError(
                    f"'{name}' requires optional dependencies. "
                    f'Install the corresponding extra (e.g. uv add wulu-geetest-bypass[{module_name}]). '
                    f'Underlying error: {err}'
                ) from err

            return _missing_dependency_stub

    raise AttributeError(f'module {__name__!r} has no attribute {name!r}')


def __dir__():
    return __all__
