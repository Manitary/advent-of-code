F:=Open("input4.txt","r");
bounds:=Split(Gets(F),"-");

procedure TestDigit(~code,idx,~candidates,part)
	for d in [i:i in [idx eq 1 select 1 else code[idx-1]..9]] do
		code[idx]:=d;
		if [code[i]:i in [1..idx]] ge [StringToInteger(bounds[1,i]):i in [1..idx]] and [code[i]:i in [1..idx]] le [StringToInteger(bounds[2,i]):i in [1..idx]] then
			if idx eq 6 then
				if part eq 1 then
					if exists(i){x:x in [1..5]|code[x] eq code[x+1]} then
						candidates+:=1;
					end if;
				elif part eq 2 then
					if 2 in Multiplicities({*x:x in code*}) then
						candidates+:=1;
					end if;
				end if;
			else
				TestDigit(~code,idx+1,~candidates,part);
			end if;
		end if;
	end for;
end procedure;

code:=[0:i in [1..6]];
candidates:=0;
TestDigit(~code,1,~candidates,1);
PrintFile("day04.txt",candidates);
candidates:=0;
TestDigit(~code,1,~candidates,2);
PrintFile("day04.txt",candidates);
