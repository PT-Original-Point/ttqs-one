# R07 Word render provenance

The packaged `render_docx.py` was attempted first and could not run because `soffice.exe` is not installed on this Windows host. The candidate was therefore opened read-only in a separate hidden Microsoft Word COM 16.0 instance (no pre-existing WINWORD process was observed), exported to PDF, then rasterized at 150 DPI with the bundled Poppler `pdftoppm.exe`.

The R06 parent was rendered with the same Word version and export settings. All twelve page PNGs were compared by SHA-256: pages 1–10 and 12 are byte-identical; only page 11 changed. The R07 page 11 image was visually inspected at original resolution. Rendered PDF/PNG files remain local QA intermediates; their hashes and comparison are recorded in the visual receipts.
