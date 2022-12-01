F:=Open("input25.txt","r");
stars:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~stars,[StringToInteger(c):c in Split(s,",")]);
end while;

dist:=func<a,b|&+[Abs(a[i]-b[i]):i in [1..#a]]>;

G:=EmptyGraph(#stars);

for i in [1..#stars-1], j in [i+1..#stars] do
	if dist(stars[i],stars[j]) le 3 then
		G+:={{i,j}};
	end if;
end for;

PrintFile("day25.txt",#ConnectedComponents(G));
