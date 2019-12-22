F:=Open("input21.txt","r");
program:=eval("[" cat Gets(F) cat "]");

function GetMemory(list,idx)
	if IsDefined(list,idx) then
		return list[idx];
	else
		return 0;
	end if;
end function;

function ChooseMode(value,mode,seq,base)
	if mode eq "1" then
		return value;
	elif mode eq "0" then
		return GetMemory(seq,value+1);
	elif mode eq "2" then
		return GetMemory(seq,base+value+1);
	end if;
end function;

procedure ExecuteCode(~list,~pos,~base,~done,input,~output,~idx)
	instruction:=IntegerToString(list[pos]);
	while #instruction lt 5 do
		instruction:="0"*instruction;
	end while;
	jump:=0;
	command:=StringToInteger(Substring(instruction,4,2));
	case command:
		when 1:
			list[list[pos+3]+1+(instruction[1] eq "2" select base else 0)]:=(ChooseMode(list[pos+1],instruction[3],list,base))+(ChooseMode(list[pos+2],instruction[2],list,base));
			jump:=4;
		when 2:
			list[list[pos+3]+1+(instruction[1] eq "2" select base else 0)]:=(ChooseMode(list[pos+1],instruction[3],list,base))*(ChooseMode(list[pos+2],instruction[2],list,base));
			jump:=4;
		when 3:
			list[list[pos+1]+1+(instruction[3] eq "2" select base else 0)]:=input[idx];
			idx+:=1;
			jump:=2;
		when 4:
			output cat:=[ChooseMode(list[pos+1],instruction[3],list,base)];
			jump:=2;
		when 5:
			if ChooseMode(list[pos+1],instruction[3],list,base) ne 0 then
				pos:=ChooseMode(list[pos+2],instruction[2],list,base)+1;
				jump:=0;
			else
				jump:=3;
			end if;
		when 6:
			if ChooseMode(list[pos+1],instruction[3],list,base) eq 0 then
				pos:=ChooseMode(list[pos+2],instruction[2],list,base)+1;
				jump:=0;
			else
				jump:=3;
			end if;
		when 7:
			list[list[pos+3]+1+(instruction[1] eq "2" select base else 0)]:=ChooseMode(list[pos+1],instruction[3],list,base) lt ChooseMode(list[pos+2],instruction[2],list,base) select 1 else 0;
			jump:=4;
		when 8:
			list[list[pos+3]+1+(instruction[1] eq "2" select base else 0)]:=ChooseMode(list[pos+1],instruction[3],list,base) eq ChooseMode(list[pos+2],instruction[2],list,base) select 1 else 0;
			jump:=4;
		when 9:
			base+:=ChooseMode(list[pos+1],instruction[3],list,base);
			jump:=2;
		when 99:
			done:=true;
	end case;
	if command notin {1..9} join {99} then
		print "error:",list[pos];
	end if;
	pos+:=jump;
end procedure;

list:=program;
base:=0;
pos:=1;
done:=false;
idx:=1;
output:=[];

instructions:=["NOT A J","NOT B T","OR T J","NOT C T","OR T J","NOT D T","NOT T T","AND T J","WALK"];
input:=&cat[[StringToCode(s[i]):i in [1..#s]] cat [10]:s in instructions];

repeat
	ExecuteCode(~list,~pos,~base,~done,input,~output,~idx);
until done;

//&*[CodeToString(c):c in output];
PrintFile("day21.txt",output[#output]);



list:=program;
base:=0;
pos:=1;
done:=false;
idx:=1;
output:=[];

instructions:=["NOT E J","NOT H T","AND T J","NOT J J","NOT A T","NOT T T","AND B T","AND C T","NOT T T","AND T J","AND D J","RUN"];
input:=&cat[[StringToCode(s[i]):i in [1..#s]] cat [10]:s in instructions];

repeat
	ExecuteCode(~list,~pos,~base,~done,input,~output,~idx);
until done;

//&*[CodeToString(c):c in output];
PrintFile("day21.txt",output[#output]);
