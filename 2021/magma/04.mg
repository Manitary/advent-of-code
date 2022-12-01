F:=Open("input4.txt","r");

SplitInput:=func<x|[StringToInteger(c):c in Split(x, " ,")]>;

numbers:=SplitInput(Gets(F));

boards:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	if #s eq 0 then
		Append(~boards,[]);
	else
		Append(~boards[#boards],SplitInput(s));
	end if;
end while;

procedure UpdateBoards(~l, n)
	for j in [1..#l] do
		for i in [1..#l[j]] do
			p:=Index(l[j,i],n);
			if p gt 0 then
				l[j,i,p]:=-1;
				break;
			end if;
		end for;
	end for;
end procedure;

function WinningBoard(b)
	pattern:=[-1:i in [1..#b]];
	for i in [1..#b] do
		if b[i] eq pattern or [b[j,i]:j in [1..#b]] eq pattern then
			return true, &+[&+[x gt 0 select x else 0:x in r]:r in b];
		end if;
	end for;
	return false, 0;
end function;

scores:=[];
for n in numbers do
	UpdateBoards(~boards, n);
	for b in boards do
		w, s:=WinningBoard(b);
		if w then
			Append(~scores,s*n);
			Exclude(~boards,b);
		end if;
	end for;
end for;

PrintFile("day04.txt", scores[1]);
PrintFile("day04.txt", scores[#scores]);
