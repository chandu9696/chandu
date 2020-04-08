
<html>
<head>
Array deletion
</head>
<?php
$ele = 'jan';

$months = array('jan', 'feb', 'march', 'april'); 
foreach (array_keys($months, $delete_item) as $key) {
    unset($months[$key]);
}
var_dump($months);
?>
</html>