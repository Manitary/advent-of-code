input:=[["set","b","99"],["set","c","b"],["jnz","a","2"],["jnz","1","5"],["mul","b","100"],["sub","b","-100000"],["set","c","b"],["sub","c","-17000"],["set","f","1"],["set","d","2"],["set","e","2"],["set","g","d"],["mul","g","e"],["sub","g","b"],["jnz","g","2"],["set","f","0"],["sub","e","-1"],["set","g","e"],["sub","g","b"],["jnz","g","-8"],["sub","d","-1"],["set","g","d"],["sub","g","b"],["jnz","g","-13"],["jnz","f","2"],["sub","h","-1"],["set","g","b"],["sub","g","c"],["jnz","g","2"],["jnz","1","3"],["sub","b","-17"],["jnz","1","-23"]];

function getvalue(string,registers,values)
	if Regexp("[0-9]+",string) then
		return StringToInteger(string);
	else
		return values[Index(registers,string)];
	end if;
end function;

procedure execute(input,~command_num,registers,~values,~mul_count)
	command:=input[command_num];
	case command[1]:
		when "set":
			values[Index(registers,command[2])]:=getvalue(command[3],registers,values);
		when "sub":
			values[Index(registers,command[2])]-:=getvalue(command[3],registers,values);
		when "mul":
			values[Index(registers,command[2])]*:=getvalue(command[3],registers,values);
			mul_count+:=1;
		when "jnz":
			if getvalue(command[2],registers,values) ne 0 then
				command_num+:=getvalue(command[3],registers,values)-1;
			end if;
	end case;
	command_num+:=1;
end procedure;

registers:={};
for command in input do
	if Regexp("[a-z]",command[2]) then
		Include(~registers,command[2]);
	end if;
end for;
registers:=SetToSequence(registers);
values:=[0:register in registers];
command_num:=1;
mul_count:=0;

repeat
	execute(input,~command_num,registers,~values,~mul_count);
until command_num le 0 or command_num gt #input;
mul_count;