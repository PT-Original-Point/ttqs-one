# R02 font-floor gap analysis

- R02 candidate SHA-256: `bdb6ef07c1aacd31f638cdad511012777d2f1b9d2c9f5f307252dd62de0170a4`.
- Current Unique Blueprint criterion: body text at least 10.5 pt; tables at least 9.5 pt.
- R02 technical QA measured the table minimum (`minimum_explicit_table_font_pt=9.5`) but did not inspect body runs. Its aggregate `technical_qa.json` therefore did not detect the body-font defect.
- Direct inspection of the R02 Word body found 83 nonempty runs; 20 were below 10.5 pt (9.5 or 10.0 pt). Table content comprised 611 nonempty runs and met the 9.5 pt minimum.
- R03 raises only those 20 body runs to 10.5 pt. Its patch receipt records every affected paragraph/run and the before/after body text digest. All paragraph and table cell text is unchanged. R02 is retained as historical and its semantic PASS remains bound to the R02 exact SHA only.
- R03 has a separate technical receipt, full 14-page render inspection, and a new independent semantic review bound to the R03 exact SHA. No formal acceptance is implied.
