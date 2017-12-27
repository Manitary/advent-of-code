input:=325489;

d:=-1;
repeat
	d+:=2;
until d^2 ge input;

coord:=[Integers()!((d-1)/2),-Integers()!((d-1)/2)];
value:=d^2;

for i in [1..4] do
	for j in [1..d-1] do
		if i eq 1 then
			coord[1]-:=1;
		elif i eq 2 then
			coord[2]+:=1;
		elif i eq 3 then
			coord[1]+:=1;
		elif i eq 4 then
			coord[2]-:=1;
		end if;
		value-:=1;
		if value eq input then
			break i;
		end if;
	end for;
end for;

Abs(coord[1])+Abs(coord[2]);