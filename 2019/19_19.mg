F:=Open("input19.txt","r");
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

procedure ExecuteCode(~list,~pos,~base,~output,~done,input,~idx)
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
			output:=ChooseMode(list[pos+1],instruction[3],list,base);
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

count:=0;
output:=0;
for y in [0..49], x in [0..49] do
	list:=program;
	base:=0;
	pos:=1;
	done:=false;
	input:=[x,y];
	idx:=1;
	repeat
		ExecuteCode(~list,~pos,~base,~output,~done,input,~idx);
	until done;
	count+:=output;
end for;

PrintFile("day19.txt",count);

y:=-1;
min_x:=0;

repeat
	y+:=1;
	found:=false;
	x:=min_x;
	output:=0;
	repeat
		list:=program;
		base:=0;
		pos:=1;
		done:=false;
		input:=[x,y];
		idx:=1;
		repeat
			ExecuteCode(~list,~pos,~base,~output,~done,input,~idx);
		until done;
		x+:=1;
	until output eq 1 or x eq min_x+2;
	if output eq 1 then
		x-:=1;
		min_x:=x;
		repeat
			list:=program;
			base:=0;
			pos:=1;
			done:=false;
			input:=[x+99,y];
			idx:=1;
			repeat
				ExecuteCode(~list,~pos,~base,~output,~done,input,~idx);
			until done;
			if output eq 0 then
				break;
			end if;
			for a in {x,x+99} do
				list:=program;
				base:=0;
				pos:=1;
				done:=false;
				input:=[a,y+99];
				idx:=1;
				repeat
					ExecuteCode(~list,~pos,~base,~output,~done,input,~idx);
				until done;
				if output eq 0 then
					break a;
				end if;
				found:=true;
			end for;
			if found then
				break; 
			end if;
			x+:=1;
		until found;
	end if;
until found;

PrintFile("day19.txt",x*10000+y);
