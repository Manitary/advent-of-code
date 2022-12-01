F:=Open("input6.txt","r");
list:=[[]];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	if #s eq 0 then
		Append(~list,[]);
	else
		Append(~list[#list],s);
	end if;
end while;

PrintFile("day06.txt",&+[#SequenceToSet(Eltseq(&*entry)):entry in list]);
PrintFile("day06.txt",&+[#&meet[SequenceToSet(Eltseq(x)):x in entry]:entry in list]);
