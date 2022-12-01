F:=Open("input7.txt","r");
crabs:=[StringToInteger(c):c in Split(Gets(F), ",")];

Sort(~crabs);

cost1:=func<list,val|&+[Abs(x-val):x in list]>;
cost2:=func<list,val|&+[(Abs(x-val)*(Abs(x-val)+1)) div 2:x in list]>;

sol1:=0;
if #crabs mod 2 eq 1 then
	val:=crabs[(#crabs div 2) + 1];
	sol1:=cost1(crabs, val);
else
	val:=crabs[#crabs div 2] + crabs[(#crabs div 2) + 1];
	if val mod 2 eq 0 then
		val div:= 2;
		sol1:=cost1(crabs, val);
	else
		val div:= 2;
		sol1:=Min(cost1(crabs, val), cost1(crabs, val+1));
	end if;
end if;

PrintFile("day07.txt", sol1);

/*
mean:=&+crabs / #crabs;
cost2(crabs, Round(mean));
*/

best:=0;
for i in [Min(crabs)..Max(crabs)] do
	cost:=&+[(Abs(x-i) * (Abs(x-i)+1)) div 2 : x in crabs];
	if best eq 0 then
		best:=cost;
	else
		if cost gt best then
			PrintFile("day07.txt", best);
			break;
		end if;
		best:=cost;
	end if;
end for;
