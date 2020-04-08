<html>

<body>


<table width="400px" cellspacing="0px" cellpadding="0px" border="1px">
<?php  
for($r=1;$r<=8;$r++)  
{  
	echo "<tr>";  
	for($co=1;$co<=8;$co++)  
	{
		$t=$r+$co;
		if($t%2==0)
		{  
			echo "<td height=35px width=30px bgcolor=#FFFFFF></td>";  
		}  
		else  
		{  
			echo "<td height=35px width=30px bgcolor=#000000></td>";  
		}  
	}  
	echo "</tr>";  
}  
?>  
</table>
</body>
<html>