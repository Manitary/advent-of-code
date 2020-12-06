F:=Open("input1.txt","r");

list:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~list,StringToInteger(s));
end while;

exists(i,j){<list[x],list[y]>:y in [x+1..#list], x in [1..#list-1]|list[x]+list[y] eq 2020};
PrintFile("day01.txt",i*j);

exists(i,j,k){<list[x],list[y],list[z]>:z in [y+1..#list], y in [x+1..#list-1], x in [1..#list-2]|list[x]+list[y]+list[z] eq 2020};
PrintFile("day01.txt",i*j*k);
