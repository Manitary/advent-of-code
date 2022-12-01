input:=[["set","i","31"],["set","a","1"],["mul","p","17"],["jgz","p","p"],["mul","a","2"],["add","i","-1"],["jgz","i","-2"],["add","a","-1"],["set","i","127"],["set","p","826"],["mul","p","8505"],["mod","p","a"],["mul","p","129749"],["add","p","12345"],["mod","p","a"],["set","b","p"],["mod","b","10000"],["snd","b"],["add","i","-1"],["jgz","i","-9"],["jgz","a","3"],["rcv","b"],["jgz","b","-1"],["set","f","0"],["set","i","126"],["rcv","a"],["rcv","b"],["set","p","a"],["mul","p","-1"],["add","p","b"],["jgz","p","4"],["snd","a"],["set","a","b"],["jgz","1","3"],["snd","b"],["set","f","1"],["add","i","-1"],["jgz","i","-11"],["snd","a"],["jgz","f","-16"],["jgz","a","-19"]];

function module(input,n)
	if input mod n eq 0 then
		return n;
	else
		return input mod n;
	end if;
end function;

function getvalue(string,registers,values)
	if string in registers then
		return values[Index(registers,string)];
	else
		return StringToInteger(string);
	end if;
end function;

procedure execute(input,~order_num,registers,~values,~recovered,~played)
	order:=input[order_num];
	case order[1]:
		when "snd":
			played:=getvalue(order[2],registers,values);
		when "set":
			values[Index(registers,order[2])]:=getvalue(order[3],registers,values);
		when "add":
			values[Index(registers,order[2])]+:=getvalue(order[3],registers,values);
		when "mul":
			values[Index(registers,order[2])]*:=getvalue(order[3],registers,values);
		when "mod":
			values[Index(registers,order[2])]mod:=getvalue(order[3],registers,values);
		when "rcv":
			if getvalue(order[2],registers,values) ne 0 and played ne 0 then
				recovered:=true;
			end if;
		when "jgz":
			if getvalue(order[2],registers,values) gt 0 then
				order_num+:=getvalue(order[3],registers,values)-1;
			end if;
	end case;
	order_num:=module(order_num+1,#input);
end procedure;

registers:={};
for item in input do
	bool,_,reg:=Regexp("([a-z]+)",item[2]);
	if bool then
		Include(~registers,reg[1]);
	end if;
end for;
registers:=SetToSequence(registers);
values:=[0: register in registers];
order_num:=1;
played:=0;
recovered:=false;

repeat
	execute(input,~order_num,registers,~values,~recovered,~played);
until recovered;
played;
