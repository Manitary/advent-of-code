F:=Open("input8.txt","r");

input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~input, [[{z:z in Eltseq(y)}:y in Split(x, " ")]:x in Split(s, "|")]);
end while;

easycount:=0;
for line in input do
	for word in line[2] do
		if #word in {2,3,4,7} then
			easycount+:=1;
		end if;
	end for;
end for;

PrintFile("day08.txt",easycount);

function FindMap(list)
	L:=AssociativeArray();
	L[Representative({w:w in list|#w eq 2})]:=1;
	L[Representative({w:w in list|#w eq 3})]:=7;
	L[Representative({w:w in list|#w eq 4})]:=4;
	L[Representative({w:w in list|#w eq 7})]:=8;
	for w in {x:x in list|#x eq 6} do
		if Representative({f:f in Keys(L)|L[f] eq 4}) subset w then
			L[w]:=9;
		elif Representative({f:f in Keys(L)|L[f] eq 1}) subset w then
			L[w]:=0;
		else
			L[w]:=6;
		end if;
	end for;
	for w in {x:x in list|#x eq 5} do
		if Representative({f:f in Keys(L)|L[f] eq 1}) subset w then
			L[w]:=3;
		elif #(Representative({f:f in Keys(L)|L[f] eq 9}) diff w) eq 1 then
			L[w]:=5;
		else
			L[w]:=2;
		end if;
	end for;
	return L;
end function;

function FindNumber(list)
	Decode:=FindMap(list[1]);
	return Seqint(Reverse([Decode[x]:x in list[2]]));
end function;

sum:=0;
for i in input do
	sum+:=FindNumber(i);
end for;

PrintFile("day08.txt",sum);
