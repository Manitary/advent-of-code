F:=Open("input21.txt","r");

start:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	_, _, x:=Regexp(": ([0-9]+)", s);
	Append(~start, StringToInteger(x[1]));
end while;

p:=1;
maxDie:=100;
track:=10;

function NextPlayer(curr)
	return curr eq #start select 1 else curr+1;
end function;

function RollDie(curr)
	return curr eq maxDie select 1 else curr+1;
end function;

function Move(tile, x)
	return (tile+x) mod track eq 0 select track else (tile+x) mod track;
end function;

pos:=start;
die:=1;
scores:=[0:x in [1..#pos]];

count:=0;
repeat
	for i in [1..3] do
		count+:=1;
		pos[p]:=Move(pos[p],die);
		die:=RollDie(die);
	end for;
	scores[p]+:=pos[p];
	p:=NextPlayer(p);
until Max(scores) ge 1000;

Min(scores)*(count);

pos:=start;
states:=AssociativeArray();
states[[start[1],start[2],0,0]]:=1;

cases:=map<{3..9}->{1,3,6,7}|[<3,1>,<4,3>,<5,6>,<6,7>,<7,6>,<8,3>,<9,1>]>;

wins:=[0,0];
p:=1;

while #Keys(states) gt 0 do
	newstates:=AssociativeArray();
	for game in Keys(states) do
		for i in [3..9] do
			newgame:=game;
			newgame[p]:=Move(newgame[p], i);
			newgame[2+p]+:=newgame[p];
			if newgame[2+p] ge 21 then
				wins[p]+:=states[game]*cases(i);
			else
				if IsDefined(newstates, newgame) then
					newstates[newgame]:=newstates[newgame]+states[game]*cases(i);
				else
					newstates[newgame]:=states[game]*cases(i);
				end if;
			end if;
		end for;
	end for;
	states:=newstates;
	p:=NextPlayer(p);
end while;
Max(wins);
