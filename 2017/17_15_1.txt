input:=[883,879];
factor:=[16807,48271];
q:=2^31-1;
count:=40000000;

matching:=0;
for i in [1..count] do
	input[1]:=input[1]*factor[1] mod q;
	input[2]:=input[2]*factor[2] mod q;
	if input[1] mod 2^16 eq input[2] mod 2^16 then
		matching+:=1;
	end if;
end for;
matching;