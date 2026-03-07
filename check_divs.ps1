$lines = Get-Content "C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html"
$count = 0
$inStep3 = $false
for($i=0; $i -lt $lines.Count; $i++) {
  $line = $lines[$i]
  if($line -match 'const renderStep3') { 
    $inStep3 = $true
    $count = 0 
  }
  if($inStep3 -and $line -match '// MAIN RETURN') { break }
  if($inStep3) {
    $opens = ([regex]::Matches($line, '<div')).Count
    $closes = ([regex]::Matches($line, '</div>')).Count
    $count += $opens - $closes
    if($opens -gt 0 -or $closes -gt 0) {
      $trimmed = $line.Trim()
      if($trimmed.Length -gt 50) { $trimmed = $trimmed.Substring(0, 50) }
      Write-Host "Line $($i+1): +$opens -$closes = $count | $trimmed"
    }
  }
}