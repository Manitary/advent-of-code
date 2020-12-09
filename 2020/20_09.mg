F:=Open("input9.txt","r");

input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~input,StringToInteger(s));
end while;

for i in [26..#input] do
	if not exists(a,b){<x,y>:x in [y+1..i-1], y in [i-25..i-2]|input[x]+input[y] eq input[i]} then
		err:=i;
		PrintFile("day09.mg",input[i]);
		break i;
	end if;
end for;

for i in [err-1..1 by -1] do
	sum:=0;
	for j in [i..1 by -1] do
		sum+:=input[j];
		if sum eq input[err] then
			seq:=[input[x]:x in [j..i]];
			PrintFile("day09.mg",Min(seq)+Max(seq));
			break i;
		elif val gt input[err] then
			break j;
		end if;
	end for;
end for;
