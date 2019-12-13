F:=Open("input13.txt","r");

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

procedure ExecuteCode(~list,~pos,~base,~tiles,~data,~done)
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
			print "instruction 3";
			list[list[pos+1]+1+(instruction[3] eq "2" select base else 0)]:=1;
			jump:=2;
		when 4:
			output:=ChooseMode(list[pos+1],instruction[3],list,base);
			Append(~data,output);
			if #data eq 3 then
				if data[1] eq -1 and data[2] eq 0 then
					print "score:",data[3];
				else
					Include(~tiles,data);
				end if;
				data:=[];
			end if;
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
tiles:={};
data:=[];

repeat
	ExecuteCode(~list,~pos,~base,~tiles,~data,~done);
until done;
#{t:t in tiles|t[3] eq 2};

list:=program;
list[1]:=2;
base:=0;
pos:=1;
done:=false;
tiles:={};
data:=[];

repeat
	ExecuteCode(~list,~pos,~base,~tiles,~data,~done);
until done;
