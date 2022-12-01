F:=Open("input2.txt","r");

db:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	_, _, entry := Regexp("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)",s);
	Append(~db,entry);
end while;

count:=0;
for entry in db do
	m := Multiplicity(Eltseq(entry[4]),entry[3]);
	if m ge StringToInteger(entry[1]) and m le StringToInteger(entry[2]) then
		count+:=1;
	end if;
end for;
PrintFile("day02.txt",count);

count:=0;
for entry in db do
	check:=0;
	if entry[4][StringToInteger(entry[1])] eq entry[3] then
		check+:=1;
	end if;
	if entry[4][StringToInteger(entry[2])] eq entry[3] then
		check+:=1;
	end if;
	if check eq 1 then
		count+:=1;
	end if;
end for;
PrintFile("day02.txt",count);
