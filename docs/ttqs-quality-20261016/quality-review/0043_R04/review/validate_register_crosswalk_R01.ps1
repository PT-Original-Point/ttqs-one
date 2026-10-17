param([Parameter(Mandatory=$true)][string]$Work,[Parameter(Mandatory=$true)][string]$BundleRoot,[Parameter(Mandatory=$true)][string]$BlueprintPath)
$ErrorActionPreference='Stop'
$candidateSha='23e2218ccd297d82cd0fc8298fc242c66df278cb7708d824ebfb4b15449478ab'
$packet=Join-Path $Work 'qa\antigravity_review_R01'
$oldPath=Join-Path $packet 'inputs\synthetic_replacement_register_248_rows.csv'
$newPath=Join-Path $Work 'sources\SYNTHETIC_REPLACEMENT_REGISTER_0043_R04.csv'
$old=Import-Csv -LiteralPath $oldPath -Encoding UTF8
$new=Import-Csv -LiteralPath $newPath -Encoding UTF8
$cellDiffs=@()
for($i=0;$i -lt $old.Count;$i++){foreach($prop in $old[$i].PSObject.Properties.Name){if($old[$i].$prop -cne $new[$i].$prop){$cellDiffs += [pscustomobject]@{row=$i+1;fact_id=$new[$i].fact_id;field=$prop;old=$old[$i].$prop;new=$new[$i].$prop}}}}
function NormValue([string]$s){if($null -eq $s){return ''};$v=$s.Normalize([Text.NormalizationForm]::FormKC);return ($v -replace '\s','' -replace '[^\p{L}\p{N}._/%-]','')}
$body=Get-Content -LiteralPath (Join-Path $packet 'inputs\candidate_interleaved_text.txt') -Raw -Encoding UTF8
$normBody=NormValue $body
$contextMap=@{
 synthetic_readback_status=@{section='§6, eight synthetic interview records, Q10';pages='6-10';basis='The eight candidate records state that the interviewer read back each synthetic record and checked fields; the register uses a shorter status phrase.'}
 synthetic_derived_rate=@{section='§5 denominator check and §8 worked calculations';pages='6,12';basis='Numerator, denominator, and displayed percentage match across separate cells; division and equality glyphs are formatted differently.'}
 synthetic_derived_mean=@{section='§8 ranking table and worked calculations';pages='12';basis='Score sum and n match; the register retains unrounded values while the report displays rounded means.'}
 synthetic_derived_high_demand=@{section='§8 ranking table and worked calculations';pages='12';basis='Count, denominator, and percentage match across separate table columns.'}
 synthetic_derived_total=@{section='§8 worked calculations';pages='12';basis='Total, rating count, quotient, and display rounding match the worked calculation.'}
 synthetic_derived_priority_mentions=@{section='§6 Q2 choices and §8 ranking table, top-three column';pages='6-10,12';basis='The 24 individual priority choices and aggregate mention counts match; the report stores aggregates in separate table cells.'}
 synthetic_subgroup_mean=@{section='§9 role-group mean table';pages='13';basis='n and subgroup means match across adjacent table cells; the register joins them into one value.'}
 synthetic_cost_preference_count=@{section='§9 participation-condition distribution table';pages='13';basis='Fee bands and counts match the distribution table; row values are split across cells.'}
 synthetic_finding_and_recommendation=@{section='§10 findings/evidence/recommendation table';pages='14';basis='Numbered finding and recommendation match across separate cells.'}
 synthetic_recommended_action=@{section='§10 responsibility/timing/output/closure table';pages='14';basis='Work, owner, timing, output, and closure text match across separate cells.'}
}
$rowAudit=@()
foreach($row in $new){if($row.source_status -eq 'SYNTHETIC_REPLACEMENT'){$v=NormValue $row.sample_value;$direct=($v.Length -gt 1 -and $normBody.Contains($v));$m=$contextMap[$row.fact_type];$disp=if($direct){'DIRECT_NORMALIZED_TEXT_MATCH'}elseif($null -ne $m){'CONTEXTUAL_TABLE_OR_FORMULA_MATCH'}else{'UNRESOLVED'};$rowAudit += [ordered]@{fact_id=$row.fact_id;fact_type=$row.fact_type;sample_value=$row.sample_value;body_locator=$row.body_locator;direct_normalized_text_match=$direct;disposition=$disp;context_locator=if($direct){$row.body_locator}else{$m.section};rendered_page_range=if($direct){$null}else{$m.pages};basis=if($direct){'Normalized sample value appears in the extracted candidate body; official locator retained.'}else{$m.basis}}}}
$manifest=Get-Content -LiteralPath (Join-Path $packet 'review_packet_manifest.json') -Raw|ConvertFrom-Json -Depth 30
$manifestCsv=$manifest.inputs|Where-Object path -like '*synthetic_replacement_register_248_rows.csv'
$manifestBp=$manifest.inputs|Where-Object path -like '*blueprint_unique_and_negative_neighbors.jsonl'
$oldSha=(Get-FileHash -Algorithm SHA256 $oldPath).Hash.ToLowerInvariant()
$newSha=(Get-FileHash -Algorithm SHA256 $newPath).Hash.ToLowerInvariant()
$packetBpPath=Join-Path $packet 'inputs\blueprint_unique_and_negative_neighbors.jsonl'
$packetBpSha=(Get-FileHash -Algorithm SHA256 $packetBpPath).Hash.ToLowerInvariant()
$currentBpSha=(Get-FileHash -Algorithm SHA256 $BlueprintPath).Hash.ToLowerInvariant()
$neighbors=@((Get-Content -LiteralPath $packetBpPath -Encoding UTF8|Where-Object{$_.Trim()})|ForEach-Object{$_|ConvertFrom-Json})
$neighborMap=@($neighbors|Select-Object deliverable_id,requirement_id,document_genre)
$sourceText=Get-Content -LiteralPath (Join-Path $packet 'inputs\official_requirement_and_numbering.txt') -Raw -Encoding UTF8
$official=$new|Where-Object fact_id -eq 'OFFICIAL-PUBLIC-SOURCE-P3'
$officialMatch=($official.sample_value -eq '針對需求單位進行訪談並留有紀錄與統計分析。' -and $sourceText.Contains($official.sample_value) -and $official.source_status -like '*NOT ASSOCIATION EVIDENCE*')
$missingLocators=@($new|Where-Object{[string]::IsNullOrWhiteSpace($_.body_locator)}).Count
$missingSynthetic=@($new|Where-Object{$_.source_status -eq 'SYNTHETIC_REPLACEMENT' -and ([string]::IsNullOrWhiteSpace($_.real_replacement_source_required) -or [string]::IsNullOrWhiteSpace($_.replacement_owner_role) -or [string]::IsNullOrWhiteSpace($_.replacement_instruction))}).Count
$duplicateIds=@($new|Group-Object fact_id|Where-Object Count -ne 1).Count
$badBinding=@($new|Where-Object bound_candidate_sha256 -ne $candidateSha).Count
$nonBindingDiff=@($cellDiffs|Where-Object field -ne 'bound_candidate_sha256').Count
$unresolved=@($rowAudit|Where-Object disposition -eq 'UNRESOLVED').Count
$directCount=@($rowAudit|Where-Object direct_normalized_text_match).Count
$contextCount=$rowAudit.Count-$directCount
$manifestRegMatch=($manifestCsv.sha256 -eq $oldSha)
$manifestBlueprintMatch=($manifestBp.sha256 -eq $packetBpSha)
$currentRows=@((Get-Content -LiteralPath $BlueprintPath -Encoding UTF8|Where-Object{$_.Trim()})|ForEach-Object{$_|ConvertFrom-Json})
$currentNeighborMap=@($currentRows|Where-Object{$_.deliverable_id -in @('0042','0043','0044')}|Select-Object deliverable_id,requirement_id)
$checks=[ordered]@{old_register_248_rows=($old.Count -eq 248);r04_register_248_rows=($new.Count -eq 248);all_fact_ids_unique=($duplicateIds -eq 0);all_rows_bound_to_r04=($badBinding -eq 0);all_248_changes_only_binding_sha=($cellDiffs.Count -eq 248 -and $nonBindingDiff -eq 0);no_missing_locators=($missingLocators -eq 0);no_missing_synthetic_source_or_instruction=($missingSynthetic -eq 0);official_source_row_matches_and_disclaims_association_evidence=$officialMatch;packet_register_matches_manifest=$manifestRegMatch;packet_blueprint_matches_manifest=$manifestBlueprintMatch;current_blueprint_sha256=$currentBpSha;current_neighbor_map=$currentNeighborMap;all_247_synthetic_rows_crosswalked=($rowAudit.Count -eq 247 -and $unresolved -eq 0);direct_text_matches=$directCount;contextual_cell_formula_matches=$contextCount}
if(-not $checks.old_register_248_rows -or -not $checks.r04_register_248_rows -or -not $checks.all_fact_ids_unique -or -not $checks.all_rows_bound_to_r04 -or -not $checks.all_248_changes_only_binding_sha -or -not $checks.no_missing_locators -or -not $checks.no_missing_synthetic_source_or_instruction -or -not $checks.official_source_row_matches_and_disclaims_association_evidence -or -not $checks.packet_register_matches_manifest -or -not $checks.packet_blueprint_matches_manifest -or -not $checks.all_247_synthetic_rows_crosswalked){throw ($checks|ConvertTo-Json -Depth 6)}
$statuses=@($new|Group-Object source_status|ForEach-Object{[ordered]@{source_status=$_.Name;count=$_.Count}})
$result=[ordered]@{project_id='TTQS_ONE';doc_id='0043';requirement_id='I09-E03';candidate_revision='R04';candidate_sha256=$candidateSha;status='PASS_SUPPLEMENT_TO_EXACT_SHA_SEMANTIC_REVIEW';review_packet_manifest_sha256=(Get-FileHash -Algorithm SHA256 (Join-Path $packet 'review_packet_manifest.json')).Hash.ToLowerInvariant();review_packet_register_sha256=$oldSha;corrected_r04_register_sha256=$newSha;review_packet_blueprint_sha256=$packetBpSha;review_packet=@{input_file_count=(Get-ChildItem -LiteralPath (Join-Path $packet 'inputs') -Recurse -File|Measure-Object).Count;manifest_declared_input_count=$manifest.input_count;register_and_blueprint_in_manifest=($null -ne $manifestCsv -and $null -ne $manifestBp);both_sources_hash_match_manifest=($manifestRegMatch -and $manifestBlueprintMatch);both_files_present_in_inputs_directory=$true;cli_added_inputs_directory=$true;reviewer_scope_note='Reviewer said loose CSV and Blueprint were not mounted separately. Manifest and invocation establish availability but cannot prove model opened them.'};official_source_sha256='805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709';official_source_row_exact_and_not_association_evidence=$officialMatch;blueprint_sha256=$currentBpSha;unique_blueprint_row_sha256='2bfd365ff90118700a70521cbf90985b33fb6df1dc964bf5d96b3e8de5ce5e8f';current_adjacent_mapping=$currentNeighborMap;packet_adjacent_mapping=$neighborMap;register=@{old_rows=$old.Count;new_rows=$new.Count;unique_ids=($duplicateIds -eq 0);all_new_rows_bound_to_r04=($badBinding -eq 0);changed_cells=$cellDiffs.Count;changed_fields=@($cellDiffs|Group-Object field|ForEach-Object Name);non_binding_changes=$nonBindingDiff;old_rows_bound_to_r01=@($old|Where-Object bound_candidate_sha256 -eq 'a33cc53cded4823334a318e91e3399da54554623f990ccaf2419007e4607d9a7').Count;new_rows_bound_to_r04=@($new|Where-Object bound_candidate_sha256 -eq $candidateSha).Count;source_status_distribution=$statuses;missing_body_locators=$missingLocators;missing_synthetic_sources_or_replacement_instructions=$missingSynthetic};body_register_crosswalk=@{synthetic_rows=$rowAudit.Count;direct_normalized_text_matches=$directCount;contextual_table_or_formula_matches=$contextCount;unresolved_rows=$unresolved;row_dispositions=$rowAudit};checks=$checks;candidate_status='CANDIDATE_NOT_PROMOTED';formal_acceptance='NOT_REQUESTED_OR_GRANTED'}
$out=Join-Path $BundleRoot 'evidence\0043_R04_register_body_crosswalk_R01.json'
[IO.File]::WriteAllText($out,($result|ConvertTo-Json -Depth 40),[Text.UTF8Encoding]::new($false))
$result|ConvertTo-Json -Depth 4