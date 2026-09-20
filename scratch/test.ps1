Add-Type -AssemblyName System.Drawing
$bmp = [System.Drawing.Bitmap]::new('Preview Knowledge/VI/vi-08-post-chuan-bi-lo-hang.png')
$rect = [System.Drawing.Rectangle]::new(264, 1005, 1592, 736)
$cropped = $bmp.Clone($rect, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)
$cropped.Save('assets/warehouse_hero.jpg', [System.Drawing.Imaging.ImageFormat]::Jpeg)
$cropped.Dispose()
$bmp.Dispose()
Write-Host "Saved assets/warehouse_hero.jpg from vi-08"
