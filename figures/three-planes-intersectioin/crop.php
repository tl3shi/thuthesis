<?php

for($k = 0; $k <= 4; $k++)
{
    $src_img="intersection-".strval($k).".png";
    $src_w=400; $src_h=300;
    $w = $src_w; $h = $src_h;
    $src_x = 200;
    $src_y = 170;
    $source=imagecreatefrompng($src_img);
    $croped=imagecreatetruecolor($w, $h);
    imagecopy($croped, $source, 0, 0, $src_x, $src_y, $src_w, $src_h);
    imagepng($croped, "intersection-center-".strval($k).".png");
    imagedestroy($croped);
}

?>

