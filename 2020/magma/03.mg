F:=Open("input3.txt","r");

area:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~area,s);
end while;

function TreeCount(map,slope)
	count:=0;
	pos:=[1,1];
	repeat
		if map[pos[2],pos[1]] eq "#" then
			count+:=1;
		end if;
		pos[1]+:=slope[1];
		if pos[1] gt #map[1] then
			pos[1]-:=#map[1];
		end if;

		pos[2]+:=slope[2];
	until pos[2] gt #map;
	return count;
end function;

PrintFile("day03.txt",TreeCount(area,[3,1]));

slopes:=[[1,1],[3,1],[5,1],[7,1],[1,2]];
PrintFile("day03.txt",&*[TreeCount(area,slope):slope in slopes]);
