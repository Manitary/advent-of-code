F:=Open("input2.txt","r");
input:=eval("[" cat Gets(F) cat "]");
input[2]:=12;
input[3]:=2;

procedure ExecuteCode(~list,~pos,~done,~result)
	if list[pos] eq 1 then
		list[list[pos+3]+1]:=list[list[pos+1]+1]+list[list[pos+2]+1];
	elif list[pos] eq 2 then
		list[list[pos+3]+1]:=list[list[pos+1]+1]*list[list[pos+2]+1];
	elif list[pos] eq 99 then
		done:=true;
		result:=list[1];
	end if;
	pos+:=4;
	if pos gt #list then
		pos-:=#list;
	end if;
	if not done then
		ExecuteCode(~list,~pos,~done,~result);
	end if;
end procedure;

list:=input;
sol1:=0;
pos:=1;
done:=false;

ExecuteCode(~list,~pos,~done,~sol1);

PrintFile("day02.txt",sol1);

output:=19690720;

for i,j in[0..99] do
	list:=input;
	list[2]:=i;
	list[3]:=j;
	pos:=1;
	done:=false;
	new_res:=0;
	ExecuteCode(~list,~pos,~done,~new_res);
	if list[1] eq output then
		PrintFile("day02.txt",100*i+j);
		break;
	end if;
end for;
