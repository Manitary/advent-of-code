F:=Open("input3.txt","r");
list:={};
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Include(~list,[StringToInteger(x):x in Eltseq(s)]);
end while;
l:=#Representative(list);
len:=#list;

SequenceToBinary:=func<x|SequenceToInteger(Reverse(x),2)>;

sum:=&+{Vector(x):x in list};
gamma:=SequenceToBinary([sum[i] gt len div 2 select 1 else 0:i in [1..l]]);
powercost:=gamma * (2^l - gamma - 1);
powercost;

FilterPosition:=function(list, digit, iteration)
	if iteration gt #Representative(list) then
		return list;
	end if;
	if #list eq 1 then
		return list;
	end if;
	val:=&+[x[iteration]:x in list] ge #list/2 select digit else (1-digit);
	return {x:x in list|x[iteration] eq val};
end function;

list1:=list;
for i in [1..#Representative(list1)] do
	list1:=FilterPosition(list1,1,i);
end for;

list2:=list;
for i in [1..#Representative(list2)] do
	list2:=FilterPosition(list2,0,i);
end for;

lifesupport:=SequenceToBinary(Representative(list1)) * SequenceToBinary(Representative(list2));

PrintFile("day03.txt", powercost);
PrintFile("day03.txt", lifesupport);
