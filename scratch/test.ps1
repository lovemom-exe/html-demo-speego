Add-Type -AssemblyName System.Drawing
$bmp = [System.Drawing.Bitmap]::new('Preview Knowledge/VI/vi-07-chuyenmuc-import-export-news.png')

# Find card 1 image rect:
$top = 0
$bottom = 0
$left = 0
$right = 0

for ($y = 1200; $y -lt 2500; $y += 5) {
    for ($x = 250; $x -lt 1100; $x += 5) {
        $c = $bmp.GetPixel($x, $y)
        # Check if color is not white and not section background (244,247,249)
        if (($c.R -lt 230 -or $c.G -lt 230 -or $c.B -lt 230)) {
            if ($top -eq 0 -or $y -lt $top) { $top = $y }
            if ($y -gt $bottom) { $bottom = $y }
            if ($left -eq 0 -or $x -lt $left) { $left = $x }
            if ($x -gt $right) { $right = $x }
        }
    }
    if ($top -gt 0 -and ($y - $top) -gt 500) {
        break
    }
}

Write-Host "Card 1 image approx: Left=$left, Top=$top, Right=$right, Bottom=$bottom"
$bmp.Dispose()
