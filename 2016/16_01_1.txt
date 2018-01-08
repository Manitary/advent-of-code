input:=["R3","L2","L2","R4","L1","R2","R3","R4","L2","R4","L2","L5","L1","R5","R2","R2","L1","R4","R1","L5","L3","R4","R3","R1","L1","L5","L4","L2","R5","L3","L4","R3","R1","L3","R1","L3","R3","L4","R2","R5","L190","R2","L3","R47","R4","L3","R78","L1","R3","R190","R4","L3","R4","R2","R5","R3","R4","R3","L1","L4","R3","L4","R1","L4","L5","R3","L3","L4","R1","R2","L4","L3","R3","R3","L2","L5","R1","L4","L1","R5","L5","R1","R5","L4","R2","L2","R1","L5","L4","R4","R4","R3","R2","R3","L1","R4","R5","L2","L5","L4","L1","R4","L4","R4","L4","R1","R5","L1","R1","L5","R5","R1","R1","L3","L1","R4","L1","L4","L4","L3","R1","R4","R1","R1","R2","L5","L2","R4","L1","R3","L5","L2","R5","L4","R5","L5","R3","R4","L3","L3","L2","R2","L5","L5","R3","R4","R3","R4","R3","R1"];
coord:=Matrix([[0,0]]);
dir:=Matrix([[0,1]]);
for item in input do
	if item[1] eq "R" then
		dir*:=Matrix([[0,-1],[1,0]]);
	else
		dir*:=Matrix([[0,1],[-1,0]]);
	end if;
	coord:=AddScaledMatrix(coord,StringToInteger(Substring(item,2,#item-1)),dir);
end for;
Abs(coord[1][1])+Abs(coord[1][2]);