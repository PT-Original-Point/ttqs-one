# 0056 R04 serialization attempt (superseded)

The first R04 candidate was not accepted. SHA-256: `7197cd9de68116e2dee7944c0ce46012628be2ba5962355eeed2d2ea076b8c68`.

Word COM rejected the package as corrupted. The R03 source declared namespace prefixes `w14` and `wp14` in `mc:Ignorable`; the serialized R04 XML retained those prefix names but dropped their declarations. The failed candidate and its build receipt are preserved here as historical evidence. The repair script now uses lxml and asserts that the full namespace map survives before creating a replacement candidate.
