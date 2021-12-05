F:=Open("input5.txt","r");

SplitInput:=func<x|[StringToInteger(c):c in Split(x, " ,->")]>;
lines:=[];

while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~lines, SplitInput(s));
end while;

function CountOverlaps(input: diag:=false)
	map:=AssociativeArray();
	for l in lines do
		if l[1] ne l[3] and l[2] ne l[4] and (diag select (Abs(l[1]-l[3]) ne Abs(l[2]-l[4])) else true) then
			continue;
		end if;
		dir:=Vector([Sign(l[3]-l[1]), Sign(l[4]-l[2])]);
		coord:=Vector([l[1],l[2]]);
		while true do
			if IsDefined(map, coord) then
				map[coord] := 1;
			else
				map[coord] := 0;
			end if;
			if coord eq Vector([l[3], l[4]]) then
				break;
			end if;
			coord +:= dir;
		end while;
	end for;
	return &+[map[x]:x in Keys(map)];
end function;

PrintFile("day05.txt", CountOverlaps(lines));
PrintFile("day05.txt", CountOverlaps(lines: diag:=true));
