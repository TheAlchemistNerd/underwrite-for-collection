param(
    [string]$OutputName = 'Underwrite_for_Collection_MSME_Lifecycle_White_Paper_2026-09-15.pdf'
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

if ([System.IO.Path]::GetFileName($OutputName) -ne $OutputName) {
    throw 'OutputName must be a file name without directory components.'
}

$buildDirectory = $PSScriptRoot
$seriesRoot = Split-Path -Parent $buildDirectory
$projectRoot = Split-Path -Parent (Split-Path -Parent $seriesRoot)
$sourceDirectory = Join-Path $seriesRoot 'parts'
$tempDirectory = Join-Path $projectRoot 'scratchpad\build\underwrite-for-collection-series'
$outputDirectory = Join-Path $seriesRoot 'dist'
$assemblyPath = Join-Path $tempDirectory 'Underwrite_for_Collection_White_Paper_Assembly.md'
$outputPath = Join-Path $outputDirectory $OutputName
$corporateMetadata = Join-Path $buildDirectory 'corporate.yaml'
$headerPath = Join-Path $buildDirectory 'whitepaper-header.tex'
$mermaidFilter = Join-Path $buildDirectory 'mermaid.lua'

[System.IO.Directory]::CreateDirectory($tempDirectory) | Out-Null
[System.IO.Directory]::CreateDirectory($outputDirectory) | Out-Null

$parts = @(
    [pscustomobject]@{
        Label = 'Part 1'
        Title = 'The MSME Credit Lifecycle and Collection Cascades'
        File = 'Part_1_MSME_Credit_Lifecycle_and_Collection_Cascades.md'
    },
    [pscustomobject]@{
        Label = 'Part 2a'
        Title = 'Temporal Evidence, Behavioural Signals and Point-in-Time Feature Engineering'
        File = 'Part_2a_Temporal_Evidence_and_Feature_Engineering.md'
    },
    [pscustomobject]@{
        Label = 'Part 2b'
        Title = 'Hierarchical Bayesian Underwriting, Causal Identification and Lifecycle Dependence'
        File = 'Part_2b_Hierarchical_Bayesian_Underwriting_Causal_Identification_and_Lifecycle_Dependence.md'
    },
    [pscustomobject]@{
        Label = 'Part 3'
        Title = 'Regulatory Orchestration, Fair Intervention and Collection Governance'
        File = 'Part_3_Regulatory_Orchestration_Fair_Intervention_and_Collection_Governance.md'
    },
    [pscustomobject]@{
        Label = 'Part 4'
        Title = 'Bank-Controlled Research Sandboxes and Enterprise Credit Architecture'
        File = 'Part_4_Bank_Controlled_Research_Sandboxes_and_Enterprise_Credit_Architecture.md'
    },
    [pscustomobject]@{
        Label = 'Part 5'
        Title = 'KESONIA Pricing, Expected Credit Loss, Capital and Funding'
        File = 'Part_5_KESONIA_Pricing_Expected_Credit_Loss_Capital_and_Funding.md'
    }
)

function Remove-YamlFrontMatter {
    param([string]$Text)

    $normalised = $Text -replace "`r`n", "`n"
    if (-not $normalised.StartsWith("---`n")) {
        return $normalised
    }

    $closing = $normalised.IndexOf("`n---`n", 4, [System.StringComparison]::Ordinal)
    if ($closing -lt 0) {
        throw 'A source file has an unterminated YAML front matter block.'
    }

    return $normalised.Substring($closing + 5).TrimStart("`n")
}

function Prepare-ManuscriptBody {
    param([string]$Text)

    $body = Remove-YamlFrontMatter -Text $Text

    # Promote the manuscript's numbered section hierarchy by one Markdown level
    # so each part appears cleanly beneath its part-title leaf in the contents.
    $body = [regex]::Replace(
        $body,
        '(?m)^(#{2,6})(\s+)',
        { param($match) $match.Groups[1].Value.Substring(1) + $match.Groups[2].Value }
    )

    # References always begin on a new page and remain outside section numbering.
    $body = [regex]::Replace(
        $body,
        '(?m)^#\s+(Selected IEEE references|References)\s*$',
        '\clearpage' + [Environment]::NewLine + '# $1 {.unnumbered}'
    )

    return $body
}

$builder = [System.Text.StringBuilder]::new()
[void]$builder.AppendLine('\UnderwriteCover')
[void]$builder.AppendLine()
[void]$builder.AppendLine('\UnderwriteLicensePage')
[void]$builder.AppendLine()
[void]$builder.AppendLine('\pagenumbering{roman}')
[void]$builder.AppendLine('\gdef\CurrentPart{Contents}')
[void]$builder.AppendLine('\begingroup')
[void]$builder.AppendLine('\small')
[void]$builder.AppendLine('\setstretch{1.0}')
[void]$builder.AppendLine('\tableofcontents')
[void]$builder.AppendLine('\endgroup')
[void]$builder.AppendLine('\clearpage')
[void]$builder.AppendLine('\UnderwriteEditionStatement')
[void]$builder.AppendLine('\clearpage')
[void]$builder.AppendLine('\pagenumbering{arabic}')
[void]$builder.AppendLine()

foreach ($part in $parts) {
    $sourcePath = Join-Path $sourceDirectory $part.File
    if (-not (Test-Path -LiteralPath $sourcePath)) {
        throw "Missing source document: $sourcePath"
    }

    $body = Prepare-ManuscriptBody -Text ([System.IO.File]::ReadAllText($sourcePath))
    [void]$builder.AppendLine("\UnderwritePart{$($part.Label)}{$($part.Title)}")
    [void]$builder.AppendLine()
    [void]$builder.AppendLine($body.Trim())
    [void]$builder.AppendLine()
}

$utf8 = [System.Text.UTF8Encoding]::new($false)
[System.IO.File]::WriteAllText($assemblyPath, $builder.ToString(), $utf8)

$resourcePath = "$sourceDirectory;$seriesRoot;$projectRoot"
$pandocArguments = @(
    '--from=markdown+raw_tex+tex_math_dollars+tex_math_single_backslash+autolink_bare_uris',
    "--metadata-file=$corporateMetadata",
    "--lua-filter=$mermaidFilter",
    "--include-in-header=$headerPath",
    '--pdf-engine=xelatex',
    '--pdf-engine-opt=-halt-on-error',
    '--highlight-style=tango',
    "--resource-path=$resourcePath",
    "--output=$outputPath",
    $assemblyPath
)

Push-Location $tempDirectory
try {
    & pandoc @pandocArguments
    if ($LASTEXITCODE -ne 0) {
        throw "Pandoc failed with exit code $LASTEXITCODE."
    }
}
finally {
    Pop-Location
}

if (-not (Test-Path -LiteralPath $outputPath)) {
    throw "Expected PDF was not created: $outputPath"
}

Write-Output $outputPath
