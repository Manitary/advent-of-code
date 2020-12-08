F:=Open("input8.txt","r");

input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	i:=Substring(s,1,3);
	n:=StringToInteger(Substring(s,5,#s-4));
	Append(~input,[*i,n*]);
end while;

procedure Execute(input,~idx,~acc)
	case input[idx,1]:
		when "nop":
			idx+:=1;
		when "jmp":
			idx+:=input[idx,2];
		when "acc":
			acc+:=input[idx,2];
			idx+:=1;
	end case;
end procedure;

acc:=0;
idx:=1;
visited:={};
repeat
	Include(~visited,idx);
	Execute(input,~idx,~acc);
until idx in visited;
PrintFile("day08.txt",acc);

procedure Swap(~input,idx);
	if input[idx,1] eq "jmp" then
		input[idx,1]:="nop";
	elif input[idx,1] eq "nop" then
		input[idx,1]:="jmp";
	end if;
end procedure;

for i in [1..#input] do
	if input[i,1] ne "acc" then
		Swap(~input,i);
		acc:=0;
		idx:=1;
		visited:={};
		repeat
			Include(~visited,idx);
			Execute(input,~idx,~acc);
		until idx in visited or idx gt #input;
		if idx gt #input then
			PrintFile("day08.txt",acc);
			break i;
		end if;
		Swap(~input,i);
	end if;
end for;
