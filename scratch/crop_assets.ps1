Add-Type -AssemblyName System.Drawing

function Crop-Image($srcPath, $dstPath, $left, $top, $width, $height) {
    $bmp = [System.Drawing.Bitmap]::new($srcPath)
    $rect = [System.Drawing.Rectangle]::new($left, $top, $width, $height)
    $cropped = $bmp.Clone($rect, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)
    $cropped.Save($dstPath, [System.Drawing.Imaging.ImageFormat]::Jpeg)
    $cropped.Dispose()
    $bmp.Dispose()
    Write-Host "Saved $dstPath ($width x $height)"
}

# Crop the 2 hero images from post 09 and 10:
Crop-Image "Preview Knowledge/VI/vi-09-post-quy-trinh-nhap-kho.png" "assets/port_sunset_hero.jpg" 264 1005 1592 736
Crop-Image "Preview Knowledge/VI/vi-10-post-kiem-soat-chat-luong.png" "assets/warehouse_racks_hero.jpg" 264 1005 1592 736

# Let's also crop the hand holding card image from vi-07 card:
# In vi-07, let's find the card image bounds on card 1
$bmp = [System.Drawing.Bitmap]::new("Preview Knowledge/VI/vi-07-chuyenmuc-import-export-news.png")
# The cards are around y=1400 to 2200, card 1 left around 264
# Card image is roughly 264 to 1000 width, y around 1500 to 1900
# Let's scan
for ($y = 1400; $y -lt 1900; $y += 5) {
    $c = $bmp.GetPixel(300, $y)
    if ($c.R -lt 240 -or $c.G -lt 240 -or $c.B -lt 240) {
        $startY = $y
        break
    }
}
$bmp.Dispose()
Write-Host "vi-07 card 1 startY: $startY"
