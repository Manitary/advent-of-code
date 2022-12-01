//After interpreting the input file...
a:=0;
b:=0;
c:=0;
list:=[];
while true do;
	b:=BitwiseOr(a,65536);
	a:=1765573;
	while true do
		c:=BitwiseAnd(b,255);
		a:=BitwiseAnd(16777215,65899*BitwiseAnd(16777215,a+c));
		if b ge 256 then
			b div:=256;
		else
			break;
		end if;		
	end while;
	if a notin list then
		Append(~list,a);
	else
		break;
	end if;
end while;
PrintFile("day21.txt",list[1]);
PrintFile("day21.txt",list[#list]);
