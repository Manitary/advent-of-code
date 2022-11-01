F:=Open("input12.txt","r");

ngbh:=AssociativeArray();
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	s:=Split(s, "-");
	for i in [1,2] do
		if s[i] notin Keys(ngbh) then
			ngbh[s[i]]:={s[3-i]};
		else
			ngbh[s[i]]:=ngbh[s[i]] join {s[3-i]};
		end if;
	end for;
end while;

small:={cave:cave in Keys(ngbh)|StringToCode(cave[1]) ge 97};
big:=Keys(ngbh) diff small;

function TravelCount(cave, visited, count: bonus:=false)
	newroutes:=0;
	for new in ngbh[cave] do
		if new eq "end" then
			newroutes+:=1;
		elif new in big or (new ne "start" and bonus select true else new notin visited) then
			newroutes+:=TravelCount(new, Include(visited, new), count: bonus:=bonus and new in small and new in visited select false else bonus);
		end if;
	end for;
	return count + newroutes;
end function;

sol1:=TravelCount("start", {"start"}, 0: bonus:=false);
sol2:=TravelCount("start", {"start"}, 0: bonus:=true);

PrintFile("day12.txt", sol1);
PrintFile("day12.txt", sol2);
