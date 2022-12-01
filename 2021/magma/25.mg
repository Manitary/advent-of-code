F:=Open("input25.txt","r");

input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~input, Eltseq(s));
end while;

maxX:=#input[1];
maxY:=#input;

right:={[y,x]:y in [1..maxY], x in [1..maxX]|input[y,x] eq ">"};
down:={[y,x]:y in [1..maxY], x in [1..maxX]|input[y,x] eq "v"};

steps:=0;
while true do
	steps+:=1;
	stop:=true;
	newright:={};
	for c in right do
		next:=[c[1] ,c[2]+1 gt maxX select 1 else c[2]+1];
		if next in right or next in down then
			Include(~newright,c);
		else
			Include(~newright,next);
		end if;
	end for;
	if right ne newright then
		stop:=false;
	end if;
	right:=newright;
	newdown:={};
	for c in down do
		next:=[c[1]+1 gt maxY select 1 else c[1]+1, c[2]];
		if next in right or next in down then
			Include(~newdown,c);
		else
			Include(~newdown,next);
		end if;
	end for;
	if down ne newdown then
		stop:=false;
	end if;
	down:=newdown;
	if stop then
		break;
	end if;
	
	if steps mod 1000 eq 0 then
		steps;
	end if;
end while;

steps;
