Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Image]::FromFile('c:\Users\X1 Yoga\html speego\pages\fulfillment\vi-fulfillment.png')
$w = $img.Width
$h = $img.Height
Write-Host "Dimensions: $w x $h"

$y1 = [int]($h * 0.72)
$cropH = $h - $y1
$bmp = New-Object System.Drawing.Bitmap $w, $cropH
$g = [System.Drawing.Graphics]::FromImage($bmp)
$srcRect = New-Object System.Drawing.Rectangle 0, $y1, $w, $cropH
$dstRect = New-Object System.Drawing.Rectangle 0, 0, $w, $cropH
$g.DrawImage($img, $dstRect, $srcRect, [System.Drawing.GraphicsUnit]::Pixel)
$g.Dispose()
$img.Dispose()

$bmp.Save('c:\Users\X1 Yoga\html speego\scratch\bottom_crop.png', [System.Drawing.Imaging.ImageFormat]::Png)
$bmp.Dispose()
Write-Host "Cropped bottom saved successfully"
