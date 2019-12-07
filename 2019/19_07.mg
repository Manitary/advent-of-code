F:=Open("input7.txt","r");
program:=eval("[" cat Gets(F) cat "]");

function FixIDX(n)
	if n mod 5 eq 0 then
		return 5;
	else
		return n mod 5;
	end if;
end function;

function ChooseMode(value,mode,seq)
	if mode eq "1" then
		return value;
	elif mode eq "0" then
		return seq[value+1];
	end if;
end function;

procedure ExecuteCode(idx,~list,~pos,ID,~ID_used,~output)
	finished:=false;
	instruction:=IntegerToString(list[idx,pos[idx]]);
	while #instruction lt 5 do
		instruction:="0"*instruction;
	end while;
	jump:=0;
	command:=StringToInteger(Substring(instruction,4,2));
	case command:
		when 1:
			list[idx,list[idx,pos[idx]+3]+1]:=(ChooseMode(list[idx,pos[idx]+1],instruction[3],list[idx]))+(ChooseMode(list[idx,pos[idx]+2],instruction[2],list[idx]));
			jump:=4;
		when 2:
			list[idx,list[idx,pos[idx]+3]+1]:=(ChooseMode(list[idx,pos[idx]+1],instruction[3],list[idx]))*(ChooseMode(list[idx,pos[idx]+2],instruction[2],list[idx]));
			jump:=4;
		when 3:
			if ID_used[idx] then
				list[idx,list[idx,pos[idx]+1]+1]:=output[FixIDX(idx-1)];
			else
				list[idx,list[idx,pos[idx]+1]+1]:=ID[idx];
				ID_used[idx]:=true;
			end if;
			jump:=2;
		when 4:
			output[idx]:=ChooseMode(list[idx,pos[idx]+1],instruction[3],list[idx]);
			jump:=2;
		when 5:
			if ChooseMode(list[idx,pos[idx]+1],instruction[3],list[idx]) ne 0 then
				pos[idx]:=ChooseMode(list[idx,pos[idx]+2],instruction[2],list[idx])+1;
			else
				jump:=3;
			end if;
		when 6:
			if ChooseMode(list[idx,pos[idx]+1],instruction[3],list[idx]) eq 0 then
				pos[idx]:=ChooseMode(list[idx,pos[idx]+2],instruction[2],list[idx])+1;
			else
				jump:=3;
			end if;
		when 7:
			list[idx,list[idx,pos[idx]+3]+1]:=ChooseMode(list[idx,pos[idx]+1],instruction[3],list[idx]) lt ChooseMode(list[idx,pos[idx]+2],instruction[2],list[idx]) select 1 else 0;
			jump:=4;
		when 8:
			list[idx,list[idx,pos[idx]+3]+1]:=ChooseMode(list[idx,pos[idx]+1],instruction[3],list[idx]) eq ChooseMode(list[idx,pos[idx]+2],instruction[2],list[idx]) select 1 else 0;
			jump:=4;
		when 99:
			if idx eq 5 then
				finished:=true;
			end if;
	end case;
	pos[idx]+:=jump;
	if command in {4,99} and not finished then
		ExecuteCode(FixIDX(idx+1),~list,~pos,ID,~ID_used,~output);
	elif not finished then
		ExecuteCode(idx,~list,~pos,ID,~ID_used,~output);
	end if;
end procedure;

sol:=0;
for phase in Permutations({0..4}) do
	output:=[0:i in [1..5]];
	programs:=[program:i in [1..5]];
	ID_used:=[false:i in [1..5]];
	pos:=[1:i in [1..5]];
	ExecuteCode(1,~programs,~pos,phase,~ID_used,~output);
	sol:=Max(sol,output[5]);
end for;
PrintFile("day07.txt",sol);

sol:=0;
for phase in Permutations({5..9}) do
	output:=[0:i in [1..5]];
	programs:=[program:i in [1..5]];
	ID_used:=[false:i in [1..5]];
	pos:=[1:i in [1..5]];
	ExecuteCode(1,~programs,~pos,phase,~ID_used,~output);
	sol:=Max(sol,output[5]);
end for;
PrintFile("day07.txt",sol);
