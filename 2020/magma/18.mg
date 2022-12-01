F:=Open("input18.txt","r");

input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~input,s);
end while;

function compute(a)
	b1, x, op := Regexp("\\(([0-9+* ]+)\\)", a);
	if b1 then
		op:=op[1];
		n:=#op;
		p:=Index(a,x)+1;
		return compute(
			(p gt 2 select Substring(a,1,p-2) else "") *
			compute(op) *
			(p+n lt #a select Substring(a,p+n+1,#a-p-n) else "")
			);
	else
		b2, op := Regexp("[0-9]+ [+*] [0-9]+", a);
		if b2 then
			n:=#op;
			return compute(IntegerToString(eval op) * (n lt #a select Substring(a,n+1,#a-n) else ""));
		else
			return a;
		end if;
	end if;
end function;

PrintFile("day18.txt",&+[StringToInteger(compute(x)):x in input]);

function compute(a)
	b1, x, op := Regexp("\\(([0-9+* ]+)\\)", a);
	if b1 then
		op:=op[1];
		n:=#op;
		p:=Index(a,x)+1;
		return compute(
			(p gt 2 select Substring(a,1,p-2) else "") *
			compute(op) *
			(p+n lt #a select Substring(a,p+n+1,#a-p-n) else "")
			);
	else
		b2, op2 := Regexp("[0-9]+ \\+ [0-9]+", a);
		b3, op3 := Regexp("[0-9]+ \\* [0-9]+", a);
		if b2 then
			n:=#op2;
			p:=Index(a,op2);
			return compute(
				(p gt 1 select Substring(a,1,p-1) else "") *
				IntegerToString(eval op2) *
				(p+n lt #a select Substring(a,p+n,#a-p-n+1) else "")
				);
		elif b3 then
			n:=#op3;
			return compute(IntegerToString(eval op3) * (n lt #a select Substring(a,n+1,#a-n) else ""));
		else
			return a;
		end if;
	end if;
end function;

PrintFile("day18.txt",&+[StringToInteger(compute(x)):x in input]);
