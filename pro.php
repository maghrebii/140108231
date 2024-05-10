

<?php
echo "<table >";
$url="https://fakestoreapi.com/products";
$response=file_get_contents($url);
$val=json_decode($response,true);

foreach($val as $va){
    echo $va["title"] . "<br>";
    echo $va["price"] . "<br>". "</td></tr>";

}

    

 echo "</table>";
?>


<link rel="stylesheet " href="stylesheet1.css">
