<!DOCTYPE html>
<html lang="fi">
<head>


  <!-- Basic Page Needs
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <meta charset="utf-8">
  <title>@MarkkuOpe</title>
  <meta name="description" content="">
  <meta name="author" content="@MarkkuOpe">

  <!-- Mobile Specific Metas
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- FONT
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <link href="//fonts.googleapis.com/css?family=Raleway:400,300,600" rel="stylesheet" type="text/css">

  <!-- CSS
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
<!--  <link rel="stylesheet" href="css/normalize.css"> -->
  <link rel="stylesheet" href="css/skeleton.css">
<!--  <link rel="stylesheet" href="css/custom.css"> -->

  <script src="js/jquery.min.js"></script>




<link rel="stylesheet" href="css/default.css">
<script src="js/highlight.pack.js"></script>
<script>hljs.initHighlightingOnLoad();</script>



  <!-- Favicon
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <link rel="icon" type="image/png" href="images/favicon.png">



<style>

.buttons {

}

.targetDiv{
  display:none;
}

.tehtava{
	color: red;
	font-size:125%
}

body{
	background-color: #CEF6CE;
}

</style>


</head>


<?php

function img($f){
	echo '<a href="'.$f.'"><img class="u-full-width" src="'.$f.'"></img></a>';
}

?>



<?php
	function TableOfContents($depth, $filename)
	/*AutoTOC function written by Alex Freeman
	* Released under CC-by-sa 3.0 license
	* http://www.10stripe.com/  */
	{
	//$filename = __FILE__;
	//read in the file
	$file = fopen($filename,"r");
	$html_string = fread($file, filesize($filename));
	fclose($file);
 
	//get the headings down to the specified depth
	$pattern = '/<h[2-'.$depth.']*[^>]*>.*?<\/h[2-'.$depth.']>/';
	$whocares = preg_match_all($pattern,$html_string,$winners);
 
	//reformat the results to be more usable
	$heads = implode("\n",$winners[0]);
	$heads = str_replace('<a name="','<a href="#',$heads);
	$heads = str_replace('</a>','',$heads);
	$heads = preg_replace('/<h([1-'.$depth.'])>/','<li class="toc$1">',$heads);
	$heads = preg_replace('/<\/h[1-'.$depth.']>/','</a></li>',$heads);
 
	//plug the results into appropriate HTML tags
	$contents = '<div id="toc"> 
	<p id="toc-header">Contents</p>
	<ul>
	'.$heads.'
	</ul>
	</div>';
	echo $contents;
	}
 ?>
