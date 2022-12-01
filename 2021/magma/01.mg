F:=Open("input1.txt","r");

count_increments:=function(x)
	count:=0;
	for i in [1..#x-1] do
		if x[i] lt x[i+1] then
			count+:=1;
		end if;
	end for;
	return count;
end function;

list:=[];
sums3:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~list,StringToInteger(s));
	if #list ge 3 then
		Append(~sums3, list[#list]+list[#list-1]+list[#list-2]);
	end if;
end while;

PrintFile("day01.txt", count_increments(list));
PrintFile("day01.txt", count_increments(sums3));
