F:=Open("input5.txt","r");
input:=eval("[" cat Gets(F) cat "]");

function ChooseMode(value,mode,seq)
	if mode eq "1" then
		return value;
	elif mode eq "0" then
		return seq[value+1];
	end if;
end function;

procedure ExecuteCode(~list,pos,sol,ID)
	output:=sol;
	done:=false;
	instruction:=IntegerToString(list[pos]);
	while #instruction lt 5 do
		instruction:="0"*instruction;
	end while;
	jump:=0;
	command:=StringToInteger(Substring(instruction,4,2));
	case command:
		when 1:
			list[list[pos+3]+1]:=(ChooseMode(list[pos+1],instruction[3],list))+(ChooseMode(list[pos+2],instruction[2],list));
			jump:=4;
		when 2:
			list[list[pos+3]+1]:=(ChooseMode(list[pos+1],instruction[3],list))*(ChooseMode(list[pos+2],instruction[2],list));
			jump:=4;
		when 3:
			list[list[pos+1]+1]:=ID;
			jump:=2;
		when 4:
			output:=ChooseMode(list[pos+1],instruction[3],list);
			jump:=2;
		when 5:
			if ChooseMode(list[pos+1],instruction[3],list) ne 0 then
				pos:=ChooseMode(list[pos+2],instruction[2],list)+1;
				jump:=0;
			else
				jump:=3;
			end if;
		when 6:
			if ChooseMode(list[pos+1],instruction[3],list) eq 0 then
				pos:=ChooseMode(list[pos+2],instruction[2],list)+1;
				jump:=0;
			else
				jump:=3;
			end if;
		when 7:
			list[list[pos+3]+1]:=ChooseMode(list[pos+1],instruction[3],list) lt ChooseMode(list[pos+2],instruction[2],list) select 1 else 0;
			jump:=4;
		when 8:
			list[list[pos+3]+1]:=ChooseMode(list[pos+1],instruction[3],list) eq ChooseMode(list[pos+2],instruction[2],list) select 1 else 0;
			jump:=4;
		when 99:
			done:=true;
			PrintFile("day05.txt",output);
	end case;
	if not done then
		ExecuteCode(~list,pos+jump,output,ID);
	end if;
end procedure;

list:=input;
ExecuteCode(~list,1,0,1);

list:=input;
ExecuteCode(~list,1,0,5);
