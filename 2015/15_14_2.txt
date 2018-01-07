input:=[["Vixen","19","7","124"],["Rudolph","3","15","28"],["Donner","19","9","164"],["Blitzen","19","9","158"],["Comet","13","7","82"],["Cupid","25","6","145"],["Dasher","14","3","38"],["Dancer","3","16","37"],["Prancer","25","6","143"]];

function module(n,m)
	if n mod m eq 0 then
		return m;
	else
		return n mod m;
	end if;
end function;

input:=[[StringToInteger(input[r][i]) : i in [2..4]] : r in [1..#input]];
dist:=[0:i in [1..#input]];
score:=[0:i in [1..#input]];
t:=2503;

for s in [1..t] do
	for r in [1..#input] do
		if module(s,(input[r][2]+input[r][3])) le input[r][2] then
			dist[r]+:=input[r][1];
		end if;
	end for;
	for p in [1..#input] do
		if dist[p] eq Maximum(dist) then
			score[p]+:=1;
		end if;
	end for;
end for;
a:=Maximum(score);
a;