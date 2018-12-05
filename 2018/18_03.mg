F:=Open("input3.txt","r");
input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	_,_,t:=Regexp("([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)",s);
	Append(~input,[StringToInteger(c):c in t]);
end while;

l:=1000;
M:=ZeroMatrix(Integers(),l,l);

for m in input do
	for r in [m[2]+1..m[2]+m[4]], c in [m[1]+1..m[1]+m[3]] do
		M[r][c]+:=1;
	end for;
end for;

PrintFile("day03.txt",#{*M[i][j]:i in [1..l], j in [1..l]|M[i][j] gt 1*});

for m in input do
	found:=true;
	for r in [m[2]+1..m[2]+m[4]], c in [m[1]+1..m[1]+m[3]] do
		if M[r][c] gt 1 then
			found:=false;
			break;
		end if;
	end for;
	if found then
		PrintFile("day03.txt",Index(input,m));
		break;
	end if;
end for;
