Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

$SourceDir = $args[0]
$ZipPath = $args[1]

if (Test-Path $ZipPath) { Remove-Item $ZipPath -Force }

$zip = [System.IO.Compression.ZipFile]::Open($ZipPath, [System.IO.Compression.ZipArchiveMode]::Create)

$baseName = Split-Path $SourceDir -Leaf
$sourceFullPath = (Resolve-Path $SourceDir).Path

Get-ChildItem -Path $SourceDir -Recurse -Force -File | ForEach-Object {
    $relativePath = $_.FullName.Substring($sourceFullPath.Length).TrimStart('\', '/')
    $entryName = ($baseName + "/" + $relativePath) -replace '\\', '/'
    [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $_.FullName, $entryName, [System.IO.Compression.CompressionLevel]::Optimal) | Out-Null
}

$zip.Dispose()
Write-Host "ZIP created successfully: $ZipPath"
