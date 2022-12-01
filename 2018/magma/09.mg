F:=Open("input9.txt","r");
_,_,input:=Regexp("([0-9]+)[a-z ;]+([0-9]+)",Gets(F));
input:=[StringToInteger(n):n in input];

function traverse(c,p,s)
	if s gt 0 then
		return traverse(c,c[p][2],s-1);
	elif s lt 0 then
		return traverse(c,c[p][1],s+1);
	else
		return p;
	end if;
end function;

procedure insert(~c,l,m)
	c[m][1]:=l;
	c[m][2]:=c[l][2];
	c[c[l][2]][1]:=m;
	c[l][2]:=m;
end procedure;

procedure remove(~c,p)
	c[c[p][1]][2]:=c[p][2];
	c[c[p][2]][1]:=c[p][1];
end procedure;

function play(num_elf,num_marbles)
	circle:=[[]:i in [1..num_marbles+1]];
	circle[#circle]:=[1,1];
	circle[1]:=[#circle,#circle];
	elf:=2;
	current:=1;
	score:=[0:i in [1..num_elf]];
	for i in [2..num_marbles] do
		if i mod 23 eq 0 then
			current:=traverse(circle,current,-7);
			score[elf]+:=i+current;
			remove(~circle,current);
			current:=traverse(circle,current,1);
		else
			insert(~circle,traverse(circle,current,1),i);
			current:=traverse(circle,current,2);
		end if;
		elf:=elf eq num_elf select 1 else elf+1;
	end for;
	return Max(score);
end function;

PrintFile("day09.txt",play(input[1],input[2]));
PrintFile("day09.txt",play(input[1],input[2]*100));
