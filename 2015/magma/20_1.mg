input:=33100000;

n:=0;
repeat
	n+:=1;
until SumOfDivisors(n)*10 ge input;
n;