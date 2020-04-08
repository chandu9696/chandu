<html>
<head>
<title>PHP BILL CALCULATION</title>
</head>
<body>
<?php
$unit=122;
if($unit<=50)
{
  $bill=$unit*3.50;
  echo $bill;
  
  
}elseif($unit>50&&$unit<=150)
{
  $bill=$unit*4.00;
  echo $bill;
  
}elseif($unit>150&&$unit<=250)
{
  $bill=$unit*5.20;
  echo $bill;
  
}else
{
  $bill=$unit*6.50;
  echo $bill;
}
?>
</body>
</html>