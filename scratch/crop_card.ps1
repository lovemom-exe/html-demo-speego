Add-Type -AssemblyName System.Drawing
$bmp = [System.Drawing.Bitmap]::new('Preview Knowledge/VI/vi-07-chuyenmuc-import-export-news.png')
# Card 1 image is at 310, 1210 with width ~785, height ~405
# Let's crop it cleanly
$rect = [System.Drawing.Rectangle]::new(310, 1210, 785, 405)
$cropped = $bmp.Clone($rect, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)
$cropped.Save('assets/card_hand_device.jpg', [System.Drawing.Imaging.ImageFormat]::Jpeg)
$cropped.Dispose()
$bmp.Dispose()
Write-Host "Saved assets/card_hand_device.jpg"
