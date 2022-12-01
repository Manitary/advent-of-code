F:=Open("input13.txt","r");

dots:={};
while true do
	s:=Gets(F);
	if #s eq 0 then
		break;
	end if;
	Include(~dots, [StringToInteger(c):c in Split(s, ",")]);
end while;

instructions:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	s:=Split(s, " =");
	Append(~instructions, [s[3] eq "x" select 1 else 2, StringToInteger(s[4])]);
end while;

for i in instructions do
	dots:={[j eq i[1] select (p[j] gt i[2] select i[2]*2-p[j] else p[j]) else p[j]:j in [1,2]]:p in dots};
	if Index(instructions,i) eq 1 then
		PrintFile("day13.txt", #dots);
	end if;
end for;

x1:=Max([p[1]:p in dots]);
y1:=Max([p[2]:p in dots]);

PrintFile("day13.txt","");
for y in [0..y1] do
	line:="";
	for x in [0..x1] do
		if [x,y] in dots then
			line*:="#";
		else
			line*:=".";
		end if;
	end for;
	PrintFile("day13.txt",line);
end for;
