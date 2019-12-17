F:=Open("input17.txt","r");
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

procedure ExecuteCode(~list,~pos,~base,~tiles,~data,~done,input,~idx)
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
			//print "receiving input";
			list[list[pos+1]+1+(instruction[3] eq "2" select base else 0)]:=input[idx];
			idx+:=1;
			jump:=2;
		when 4:
			output:=ChooseMode(list[pos+1],instruction[3],list,base);
			//print "output:",output;
			if output eq 10 then
				Append(~data,[]);
			else
				Append(~data[#data],output);
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
data:=[[]];
idx:=1;

repeat
	ExecuteCode(~list,~pos,~base,~tiles,~data,~done,0,~idx);
until done;

alignment:=0;
for i in [2..#data-3], j in [2..#data[1]-1] do
	if data[i,j] eq 35 then
		if {data[a,b]:a in [i-1..i+1],b in [j-1..j+1]|Abs(a-i)+Abs(b-j) eq 1} eq {35} then
			alignment+:=(i-1)*(j-1);
		end if;
	end if;
end for;

PrintFile("day17.txt",alignment);

/*
for line in data do
	if #line gt 0 then
		print &*[CodeToString(c):c in line];
	end if;
end for;
*/

list:=program;
list[1]:=2;
base:=0;
pos:=1;
done:=false;
data:=[[]];

idx:=1;

routine:="A,B,A,C,B,C,B,C,A,C";
move_A:="R,12,L,6,R,12";
move_B:="L,8,L,6,L,10";
move_C:="R,12,L,10,L,6,R,10";
camera_feed:="n";
input:=&cat[[StringToCode(c):c in Eltseq(s)] cat [10]:s in [routine,move_A,move_B,move_C,camera_feed]];

repeat
	ExecuteCode(~list,~pos,~base,~tiles,~data,~done,input,~idx);
until done;

PrintFile("day17.txt",data[#data,1]);
