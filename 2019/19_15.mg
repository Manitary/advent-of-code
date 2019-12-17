F:=Open("input15.txt","r");

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

function GetDir(dir)
	case dir:
		when 1: return Vector([0,1]);
		when 2: return Vector([0,-1]);
		when 3: return Vector([-1,0]);
		when 4: return Vector([1,0]);
	end case;
	print "input error";
	return false;
end function;

function PrintMap(coords,map,droid)
	minX:=Min({v[1]:v in coords});
	maxX:=Max({v[1]:v in coords});
	minY:=Min({v[2]:v in coords});
	maxY:=Max({v[2]:v in coords});
	for y in [maxY..minY by -1] do
		line:="";
		for x in [minX..maxX] do
			if Vector([x,y]) in coords then
				if droid eq Vector([x,y]) then
					line*:="D";
				else
					line*:=map[Vector([x,y])];
				end if;
			else
				line*:=" ";
			end if;
		end for;
		print line;
	end for;
	return true;
end function;

procedure ExecuteCode(~list,~pos,~base,~tiles,~data,~done,~dir,~droid,~keys)
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
			print "Ready for input:";
			readi input;
			list[list[pos+1]+1+(instruction[3] eq "2" select base else 0)]:=input;
			dir:=GetDir(input);
			jump:=2;
		when 4:
			output:=ChooseMode(list[pos+1],instruction[3],list,base);
			print "output:",output;
			case output:
				when 0:
					if not IsDefined(data,droid+dir) then
						data[droid+dir]:="#";
						Include(~keys,droid+dir);
					end if;
				when 1:
					if not IsDefined(data,droid+dir) then
						data[droid+dir]:=".";
						Include(~keys,droid+dir);
					end if;
					droid+:=dir;
				when 2:
					print "Oxygen found";
					if not IsDefined(data,droid+dir) then
						data[droid+dir]:="@";
						Include(~keys,droid+dir);
					end if;
					droid+:=dir;
			end case;
			PrintMap(keys,data,droid);
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
data:=AssociativeArray();
data[Vector([0,0])]:=".";
keys:={Vector([0,0])};
droid:=Vector([0,0]);
dir:=0;

repeat
	ExecuteCode(~list,~pos,~base,~tiles,~data,~done,~dir,~droid,~keys);
until done;

