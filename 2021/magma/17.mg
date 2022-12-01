F:=Open("input17.txt","r");

s:=Gets(F);
_, _, rangeX:=Regexp("x=([0-9-]+)..([0-9-]+)", s);
_, _, rangeY:=Regexp("y=([0-9-]+)..([0-9-]+)", s);
x1:=StringToInteger(rangeX[1]);
x2:=StringToInteger(rangeX[2]);
y1:=StringToInteger(rangeY[1]);
y2:=StringToInteger(rangeY[2]);

function IsInRange(x,y)
	t:=0;
	xp:=0;
	yp:=0;
	maxheight:=0;
	while yp ge y1 do
		xp+:=t le x select x-t else 0;
		yp+:=y-t;
		maxheight:=Max(maxheight, yp);
		t+:=1;
		if x1 le xp and xp le x2 and y1 le yp and yp le y2 then
			return true, maxheight;
		end if;
	end while;
	return false, 0;
end function;

bestheight:=0;
valid:=0;
for x in [0..x2], y in [y1..-y1+1] do
	check, height:=IsInRange(x,y);
	if check then
		bestheight:=Max(bestheight, height);
		valid+:=1;
	end if;
end for;

PrintFile("day17.txt", bestheight);
PrintFile("day17.txt", valid);
