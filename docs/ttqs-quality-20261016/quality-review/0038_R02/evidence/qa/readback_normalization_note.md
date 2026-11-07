# 0038 R02 initial GitHub readback reconciliation

The first readback at commit `7ca8cbe86be4cdbcb5657e4fa24543fb53181ad3` reported 25/35 manifest entries matching and 10 text entries mismatching. The DOCX, PDF, and all rendered PNGs matched their exact SHA-256 and byte lengths. Every mismatch was a text artifact whose Windows working-tree CRLF bytes had been normalized to LF in the GitHub blob.

The initial result is retained in `remote_readback_attempt_initial.json`. The verifier and manifest were corrected to compare canonical LF text bytes with the remote Git blobs. This was a manifest/readback encoding issue; it did not modify the candidate DOCX or its exact SHA-256.
