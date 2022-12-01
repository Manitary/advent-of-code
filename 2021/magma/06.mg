F:=Open("input6.txt","r");
input:=[StringToInteger(c):c in Split(Gets(F), ",")];
fishes:=[0:i in [1..9]];

for f in input do
	fishes[f+1]+:=1;
end for;

function UpdateFishes(fish)
	newfish:=[0:i in [1..9]];
	for i in [1..8] do
		newfish[i]:=fish[i+1];
	end for;
	newfish[7]+:=fish[1];
	newfish[9]+:=fish[1];
	return newfish;
end function;

n1:=80;
n2:=256;
for i in [1..n2] do
	fishes:=UpdateFishes(fishes);
	if i eq n1 or i eq n2 then
		PrintFile("day06.txt", &+fishes);
	end if;
end for;
