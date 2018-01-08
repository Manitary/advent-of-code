input:=33100000;

n:=0;
repeat
	n+:=1;
	sum:=0;
	for d in Reverse(Divisors(n)) do
		if d*50 ge n then
			sum+:=d*11;
		else
			break;
		end if;
	end for;
until sum ge input;
n;