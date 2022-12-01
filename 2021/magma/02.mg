F:=Open("input2.txt","r");

x:=0;
y:=0;
a:=0;

while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	s:=Split(s," ");
	if s[1][1] eq "f" then
		x+:=StringToInteger(s[2]);
		y+:=StringToInteger(s[2])*a;
	elif s[1][1] eq "d" then
		a+:=StringToInteger(s[2]);
	elif s[1][1] eq "u" then
		a-:=StringToInteger(s[2]);
	end if;
end while;

PrintFile("day02.txt", x*a);
PrintFile("day02.txt", x*y);
