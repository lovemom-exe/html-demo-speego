Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Image]::FromFile('c:\Users\X1 Yoga\html speego\pages\fulfillment\vi-fulfillment.png')
$w = $img.Width
$h = $img.Height

# Middle crop (from 40% to 75%)
$y1 = [int]($h * 0.40)
$cropH = [int]($h * 0.35)
$bmp = New-Object System.Drawing.Bitmap $w, $cropH
$g = [System.Drawing.Graphics]::FromImage($bmp)
$srcRect = New-Object System.Drawing.Rectangle 0, $y1, $w, $cropH
$dstRect = New-Object System.Drawing.Rectangle 0, 0, $w, $cropH
$g.DrawImage($img, $dstRect, $srcRect, [System.Drawing.GraphicsUnit]::Pixel)
$g.Dispose()
$img.Dispose()

$bmp.Save('c:\Users\X1 Yoga\html speego\scratch\middle_crop.png', [System.Drawing.Imaging.ImageFormat]::Png)
$bmp.Dispose()
Write-Host "Cropped middle saved successfully"
