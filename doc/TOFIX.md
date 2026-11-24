# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/pyblueprint/blueprint.py:25` - text colour is passed as the SVG `color` attribute (`<text color="blue">`), which does not paint text (only `fill` does), so all text renders in the default black and the `Palette.text_color` default never shows; pass `fill=color` instead (and update `tests/unit_tests/test_blueprint.py:35,41`, which assert on `attribs["color"]`).
- `src/pyblueprint/blueprint.py:25` - `Text` is created with no `insert`, so it is emitted without `x`/`y` and its baseline sits at y=0 - the glyphs are drawn above the 100x100 canvas and are invisible in `examples/empty.py`'s `hello.svg`; give it an insert point inside the drawing.

## Medium

- `src/pyblueprint/blueprint.py:20` - `background()`, `rectangle()` (line 28) and `square()` (line 31) are identical: each adds a default `svgwrite.shapes.Rect()` (a 1x1 black rect at 0,0, verified via `dwg.tostring()`); give them real geometry (background = full canvas, square = equal sides) and parameters, and test the output attributes rather than just the element count.
- `rsconstruct.toml:28` - `src_dirs` for `ruff` (and `mypy` at `rsconstruct.toml:32`) list `config`, which holds only `.lua` files, while `examples/` (real Python) is linted by neither; replace `config` with `examples`.

## Low

- `pyproject.toml:84` - `mypy_path = "src:python:scripts"` names `python/` and `scripts/` directories that do not exist here; reduce it to `"src"`.
- `src/pyblueprint/colors.py:4` - `Names` is referenced nowhere and its empty `__init__` is noise; either use it from `Palette` (`blueprint.py:11`) or delete the module (and its entry in `sphinx/pyblueprint.rst:15`).
- `examples/empty.py:6` - examples write to hard-coded `/tmp/*.svg`; take an output directory (or use the current directory) so they run on any OS and do not clobber shared paths.
- `doc/TODO.txt:1` - refers to deriving the copyright from `config/*.py`, but configs are now `config/*.lua` and `sphinx/conf.py` is a fleet-shared file; drop or rewrite the stale item.
