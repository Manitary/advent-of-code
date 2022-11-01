F:=Open("input22.txt","r");

input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	s:=Split(s," ,");
	_,_,x:=Regexp("x=([0-9.\-]+)",s[2]);
	_,_,y:=Regexp("y=([0-9.\-]+)",s[3]);
	_,_,z:=Regexp("z=([0-9.\-]+)",s[4]);
	Append(~input, <s[1] eq "on" select 1 else 0, eval "[" * x[1] * "]", eval "[" * y[1] * "]", eval "[" * z[1] * "]" >);
end while;

cube:=AssociativeArray();
#input;
l:=50;
for i in input do
	Index(input,i);
	if i[2,1] ge -l and i[2,#i[2]] le l and i[3,1] ge -l and i[3,#i[3]] le l and i[4,1] ge -l and i[4,#i[4]] le l then
		for x in i[2], y in i[3], z in i[4] do
			cube[[x,y,z]]:=i[1];
		end for;
	end if;
end for;

sum:=0;
for k in Keys(cube) do
	if cube[k] eq 1 then
		sum+:=1;
	end if;
end for;

function SumWithConflicts(i, list)
	vol:=#list[i,2] * #list[i,3] * #list[i,4];
	conflicts:=[];
	if i lt #list then
		for j in [i+1..#list] do
			intersection:=<list[j,1],[0],[0],[0]>;
			for k in [2..4] do
				intersection[k]:=SetToSequence(SequenceToSet(list[i,k]) meet SequenceToSet(list[j,k]));
			end for;
			if #intersection[2] ne 0 and #intersection[3] ne 0 and #intersection[4] ne 0 then
				Append(~conflicts, intersection);
			end if;
		end for;
	end if;
	if #conflicts ne 0 then
		for j in [1..#conflicts] do
			vol -:= SumWithConflicts(j, conflicts);
		end for;
	end if;
	return vol;
end function;

sum:=0;
for i in [1..#input] do
	i;
	if input[i,1] eq 1 then
		sum+:=SumWithConflicts(i, input);
	end if;
end for;
sum;
