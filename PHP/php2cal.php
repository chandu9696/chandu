<html>
<head>
<title>Online PHP Script Execution</title>
</head>
<body>
<?php
$opr="+";
$A=10;
$B=20;
switch($opr)
{
    case "+":echo $A+$B;
            break;
    case "-":echo $A-$B;
            break;
    case "*":echo $A*$B;
            break;
    case "/":echo $A/$B;
            break;
    default:echo "wrong choice";
}
?>
</body>
</html>