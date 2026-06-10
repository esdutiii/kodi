Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem
$z = [System.IO.Compression.ZipFile]::OpenRead($args[0])
$z.Entries | Select-Object -First 15 -Property FullName
$z.Dispose()
