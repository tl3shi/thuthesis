<?php

for($k = 0; $k <= 9; $k++)
{
    $src_img="bvh-bunny-".strval($k).".png";
    $src_w=437; $src_h=417;
    $w = $src_w; $h = $src_h;
    $src_x = 63;
    $src_y = 55;
    $source=imagecreatefrompng($src_img);
    $croped=imagecreatetruecolor($w, $h);
    imagecopy($croped, $source, 0, 0, $src_x, $src_y, $src_w, $src_h);
    imagepng($croped, "bvh-bunny-center-".strval($k).".png");
    imagedestroy($croped);
}

?>

