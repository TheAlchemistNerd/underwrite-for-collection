param([int]$Passes = 3, [string]$PythonExecutable = 'python')
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$diagramDir = Join-Path $root 'linkedin_diagrams'
$pdfDir = Join-Path $root 'publications'
New-Item -ItemType Directory -Force -Path $diagramDir, $pdfDir | Out-Null
$files = @(
    'ARTICLE_1_RCTS_CONTEXTUAL_BANDITS_CREDIT_OFFERS.md',
    'ARTICLE_2_CONTEXTUAL_BANDITS_AND_SEQUENTIAL_COLLECTION.md',
    'ARTICLE_3_REJECT_INFERENCE_AND_SELECTIVE_LABELS.md',
    'ARTICLE_4_TREASURY_ALM_STOCHASTIC_CONTROL.md',
    'ARTICLE_5_BANK_CONTROLLED_AGENTIC_AI_CREDIT_AND_TREASURY.md'
)
$combined = Join-Path $PSScriptRoot 'UNDERWRITE_FOR_COLLECTION_FIVE_ARTICLE_RESEARCH_EDITION.md'
$parts = [System.Collections.Generic.List[string]]::new()
$parts.Add("% Underwrite for Collection: Five Connected Research Articles`n% Nevil Maloba`n% 8 October 2026`n`nThis research edition connects randomized credit-offer experiments, sequential collection decisions, reject inference, Treasury/ALM control and bank-controlled agentic deployment. The five articles retain their separate decision units and carry a common evidence and governance discipline.`n`nCopyright 2026 Nevil Maloba. CC BY-NC-SA 4.0. https://creativecommons.org/licenses/by-nc-sa/4.0/`n")
$articleNumber = 0
foreach ($name in $files) {
    $articleNumber++
    $source = Join-Path $root $name
    $parts.Add("`n\newpage`n")
    $parts.Add("<!-- equation-scope: $articleNumber -->")
    $parts.Add([System.IO.File]::ReadAllText($source, [System.Text.Encoding]::UTF8))
    $appendix = Join-Path $PSScriptRoot "appendices\ARTICLE_${articleNumber}_MATHEMATICAL_APPENDIX.md"
    if (-not (Test-Path -LiteralPath $appendix)) { throw "Missing mathematical appendix: $appendix" }
    $parts.Add("`n\clearpage`n")
    $parts.Add("<!-- equation-scope: A$articleNumber -->")
    $parts.Add([System.IO.File]::ReadAllText($appendix, [System.Text.Encoding]::UTF8))
}
$utf8 = [System.Text.UTF8Encoding]::new($false)
[System.IO.File]::WriteAllText($combined, ($parts -join "`n"), $utf8)
& $PythonExecutable (Join-Path $PSScriptRoot 'typeset_math.py') $combined
if ($LASTEXITCODE -ne 0) { throw 'Mathematics preparation failed' }
$typeset = Join-Path $PSScriptRoot 'UNDERWRITE_FOR_COLLECTION_FIVE_ARTICLE_RESEARCH_EDITION_TYPESET.md'
& $PythonExecutable (Join-Path $PSScriptRoot 'number_equations.py') $typeset
if ($LASTEXITCODE -ne 0) { throw 'Equation numbering and cross-reference preparation failed' }
$typeset = Join-Path $PSScriptRoot 'UNDERWRITE_FOR_COLLECTION_FIVE_ARTICLE_RESEARCH_EDITION_NUMBERED.md'
$env:MERMAID_OUTDIR = $diagramDir
$env:MERMAID_PUPPETEER_CONFIG = Join-Path $PSScriptRoot 'puppeteer.json'
$env:MERMAID_ARTICLE = 'underwrite_for_collection'
$env:MERMAID_NAMES = '01_offer_experiment_and_governed_learning|02_temporal_graph_bandits_mcts_graphsvx|02_evidence_to_sequential_collection_control|03_reject_inference_evidence_path|04_treasury_data_to_alco_approval|04_treasury_constrained_control_loop|05_bank_controlled_agentic_ai_workflow'
$env:MERMAID_CAPTIONS = 'Offer experiment and governed learning|Temporal graphs, bandits, MCTS and GraphSVX|Evidence-to-sequential-control pathway|Reject-inference evidence pathway|Treasury data to ALCO approval|Treasury constrained control loop|Bank-controlled agentic AI workflow'
$env:MERMAID_COVER_NAMES = '01_offer_experiment_and_governed_learning|02_temporal_graph_bandits_mcts_graphsvx|03_reject_inference_evidence_path|04_treasury_data_to_alco_approval'
$env:MERMAID_COVER_CAPTIONS = 'Article 1: offer experiment and governed learning|Article 2: temporal graph, one-step bandits and sequential search|Article 3: observed and unobserved repayment evidence|Article 4: Treasury data, constraints and ALCO approval'
$env:MERMAID_IMAGE_PREFIX = 'linkedin_diagrams/'
$filter = Join-Path $PSScriptRoot 'mermaid.lua'
$pdf = Join-Path $pdfDir 'UNDERWRITE_FOR_COLLECTION_FIVE_ARTICLE_RESEARCH_EDITION_2026-10-08.pdf'
$tex = Join-Path $PSScriptRoot 'UNDERWRITE_FOR_COLLECTION_FIVE_ARTICLE_RESEARCH_EDITION_2026-10-08.tex'
$resourcePath = "$root;$diagramDir"
$pandocArgs = @(
    $typeset, '--from=markdown+autolink_bare_uris+tex_math_dollars-implicit_figures', '--to=latex', '--standalone', '--pdf-engine=xelatex',
    "--lua-filter=$filter", "--resource-path=$resourcePath", '--toc', '--toc-depth=2',
    "--include-in-header=$(Join-Path $PSScriptRoot 'publication-header.tex')",
    '--variable=geometry:margin=0.7in', '--variable=mainfont:Segoe UI', '--variable=fontsize:11pt',
    '--metadata=lang:en', '--variable=graphics:true', '--output', $tex
)
& pandoc @pandocArgs
if ($LASTEXITCODE -ne 0) { throw "Pandoc/XeLaTeX failed with exit code $LASTEXITCODE" }
Push-Location -LiteralPath $root
try {
    for ($pass = 1; $pass -le $Passes; $pass++) {
        & xelatex -halt-on-error -interaction=nonstopmode "-output-directory=$PSScriptRoot" $tex
        if ($LASTEXITCODE -ne 0) { throw "XeLaTeX failed on pass $pass" }
    }
} finally { Pop-Location }
Copy-Item -LiteralPath ([IO.Path]::ChangeExtension($tex, '.pdf')) -Destination $pdf -Force
Remove-Item Env:MERMAID_OUTDIR,Env:MERMAID_ARTICLE,Env:MERMAID_NAMES,Env:MERMAID_CAPTIONS,Env:MERMAID_COVER_NAMES,Env:MERMAID_COVER_CAPTIONS,Env:MERMAID_IMAGE_PREFIX -ErrorAction SilentlyContinue
Write-Output "Created $pdf"
