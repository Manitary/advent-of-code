F:=Open("input4.txt","r");
input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	_,_,t:= Regexp("\\[([0-9]+)-([0-9]+)-([0-9]+) ([0-9]+):([0-9]+)] (.*)",s);
	Append(~input,t);
end while;
Sort(~input);

guards:=[];
times:=[];
for e in input do
	b,n:=Regexp("[0-9]+",e[6]);
	if b then
		id:=StringToInteger(n);
		if id notin guards then
			Append(~guards,id);
			Append(~times,[0:i in [1..60]]);
		end if;
	end if;
	sleep:=Regexp("asleep",e[6]);
	if sleep then
		sleep_start:=StringToInteger(e[5]);
	end if;
	if Regexp("wakes",e[6]) then
		for t in [sleep_start+1..StringToInteger(e[5])] do
			times[Index(guards,id)][t]+:=1;
		end for;
	end if;
end for;

_,worst:=Max([&+c:c in times]);
_,m:=Max(times[worst]);
PrintFile("day04.txt",guards[worst]*(m-1));

t,m:=Max([Max(c):c in [[times[i][j]:i in [1..#guards]]:j in [1..60]]]);
PrintFile("day04.txt",Explode([guards[i]:i in [1..#guards]|times[i][m] eq t])*(m-1));
