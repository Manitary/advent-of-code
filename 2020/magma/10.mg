F:=Open("input10.txt","r");

input:=[0];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~input,StringToInteger(s));
end while;

Sort(~input);
Append(~input,Max(input)+3);
delta:=[input[x+1]-input[x]:x in [1..#input-1]];
Multiplicity(delta,1)*Multiplicity(delta,3);

comb:=[0:i in [1..#input]];
comb[#input]:=1;
for i in [#input-1..1 by -1] do
	for j in [x:x in [i+1..i+3]|x le #input] do
		if input[j]-input[i] le 3 then
			comb[i]+:=comb[j];
		end if;
	end for;
end for;
