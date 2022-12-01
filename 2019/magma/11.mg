F:=Open("input11.txt","r");
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

procedure SwapState(~state)
	if state eq "draw" then
		state:="move";
	else
		state:="draw";
	end if;
end procedure;

procedure Rotate(n,~dir)
	if n eq 1 then
		dir*:=Matrix([[0,1],[-1,0]]);
	elif n eq 0 then
		dir*:=Matrix([[0,-1],[1,0]]);
	end if;
end procedure;

procedure ExecuteCode(~list,~pos,~base,~state,~coord,~dir,~painted,~white,~done)
	instruction:=IntegerToString(list[pos]);
	while #instruction lt 5 do
		instruction:="0"*instruction;
	end while;
	jump:=0;
	command:=StringToInteger(Substring(instruction,4,2));
	//print instruction;
	case command:
		when 1:
			list[list[pos+3]+1+(instruction[1] eq "2" select base else 0)]:=(ChooseMode(list[pos+1],instruction[3],list,base))+(ChooseMode(list[pos+2],instruction[2],list,base));
			jump:=4;
		when 2:
			list[list[pos+3]+1+(instruction[1] eq "2" select base else 0)]:=(ChooseMode(list[pos+1],instruction[3],list,base))*(ChooseMode(list[pos+2],instruction[2],list,base));
			jump:=4;
		when 3:
			list[list[pos+1]+1+(instruction[3] eq "2" select base else 0)]:=coord in white select 1 else 0;
			jump:=2;
		when 4:
			output:=ChooseMode(list[pos+1],instruction[3],list,base);
			if state eq "draw" then
				Include(~painted,coord);
				if output eq 1 then
					Include(~white,coord);
				else
					Exclude(~white,coord);
				end if;
			else
				Rotate(output,~dir);
				coord+:=dir;
			end if;
			SwapState(~state);
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
coord:=Vector([0,0]);
painted:={};
white:={};
dir:=Vector([0,1]);
state:="draw";
base:=0;
pos:=1;
done:=false;

repeat
	ExecuteCode(~list,~pos,~base,~state,~coord,~dir,~painted,~white,~done);
until done;
PrintFile("day11.txt",#painted);

list:=program;
coord:=Vector([0,0]);
painted:={};
white:={coord};
dir:=Vector([0,1]);
state:="draw";
base:=0;
pos:=1;
done:=false;

repeat
	ExecuteCode(~list,~pos,~base,~state,~coord,~dir,~painted,~white,~done);
until done;

x1:=Min({w[1]:w in white});
x2:=Max({w[1]:w in white});
y1:=Min({w[2]:w in white});
y2:=Max({w[2]:w in white});

for y in [y2..y1 by -1] do
	line:="";
	for x in [x2..x1 by -1] do
		if Vector([x,y]) in white then
			line*:="#";
		else
			line*:=" ";
		end if;
	end for;
	PrintFile("day11.txt",line);
end for;
