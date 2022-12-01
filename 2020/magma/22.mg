F:=Open("input22.txt","r");

decks:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	if #s gt 0 then
		if s[1] eq "P" then	
			Append(~decks,[]);
		else
			Append(~decks[#decks],StringToInteger(s));
		end if;
	end if;
end while;

procedure PlayTurn(~decks)
	if decks[1,1] gt decks[2,1] then
		decks[1] cat:= [decks[1,1],decks[2,1]];
	elif decks[2,1] gt decks[1,1] then
		decks[2] cat:= [decks[2,1],decks[1,1]];
	end if;
	Remove(~decks[1],1);
	Remove(~decks[2],1);
end procedure;

function Score(decks)
	score:=0;
	if #decks[1] ne 0 and #decks[2] ne 0 then
		winner:=decks[1];
	else
		exists(winner){d:d in decks|#d ne 0};
	end if;
	for i in [1..#winner] do
		score+:=i*winner[#winner-i+1];
	end for;
	return score;
end function;

old:=decks;

repeat
	PlayTurn(~decks);
until #decks[1] eq 0 or #decks[2] eq 0;
PrintFile("day22.txt",Score(decks));

procedure PlayGame(~decks,~game,~states,~roundwin,~winner)
	if #decks[game,1] eq 0 then
		winner[game]:=2;
	elif
		#decks[game,2] eq 0 or decks[game] in states[game] then
		winner[game]:=1;
	else
		Include(~states[game],decks[game]);
		if decks[game,1,1] lt #decks[game,1] and decks[game,2,1] lt #decks[game,2] then
			game+:=1;
			Append(~states,{});
			decks[game]:=[[decks[game-1,p,i]:i in [2..1+decks[game-1,p,1]]]:p in [1,2]];
			PlayGame(~decks,~game,~states,~roundwin,~winner);
			roundwin:=winner[game];
			Prune(~states);
			Prune(~decks);
			game-:=1;
		else
			roundwin:=decks[game,1,1] gt decks[game,2,1] select 1 else 2;
		end if;
		decks[game,roundwin] cat:= [decks[game,roundwin,1],decks[game,roundwin eq 1 select 2 else 1,1]];
		Remove(~decks[game,1],1);
		Remove(~decks[game,2],1);
		PlayGame(~decks,~game,~states,~roundwin,~winner);
	end if;
end procedure;

decks:=[old];
states:=[*{}*];
game:=1;
roundwin:=0;
winner:=[];
repeat
	PlayGame(~decks,~game,~states,~roundwin,~winner);
until IsDefined(winner,1);
PrintFile("day22.txt",Score(decks[1]));
