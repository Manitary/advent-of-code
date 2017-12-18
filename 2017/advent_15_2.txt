input:=[883,879];
factor:=[16807,48271];
q:=2^31-1;
count:=5000000;

procedure evolve(~input,factor,q)
	repeat
		input[1]:=input[1]*factor[1] mod q;
	until IsDivisibleBy(input[1],4);
	repeat
		input[2]:=input[2]*factor[2] mod q;
	until IsDivisibleBy(input[2],8);
end procedure;

matching:=0;
for i in [1..count] do
	evolve(~input,factor,q);
	if input[1] mod 2^16 eq input[2] mod 2^16 then
		matching+:=1;
		i;
	end if;
end for;
matching;