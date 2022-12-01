F:=Open("input11.txt","r");

input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~input, [StringToInteger(c):c in Eltseq(s)]);
end while;

Step:=function(board)
	new:=[[c+1:c in r]:r in board];
	flashes:=0;
	while exists(r,c){<x,y>:x in [1..#board], y in [1..#board[1]]|new[x,y] gt 9} do
		for i,j in [-1..1] do
			if r+i ge 1 and r+i le #board and c+j ge 1 and c+j le #board[1] then
				if new[r+i,c+j] ne -1 then
					new[r+i,c+j]+:=1;
				end if;
			end if;
		end for;
		new[r,c]:=-1;
		flashes+:=1;
	end while;
	for i in [1..#board], j in [1..#board[1]] do
		if new[i,j] eq -1 then
			new[i,j]:=0;
		end if;
	end for;
	return new, flashes;
end function;

count:=0;
board:=input;
i:=0;

while true do
	i+:=1;
	board, newflash:=Step(board);
	if i le 100 then
		count+:=newflash;
	end if;
	if newflash eq #board * #board[1] then
		print i;
		if i ge 100 then
			break;
		end if;
	end if;
end while;

PrintFile("day11.txt", count);
PrintFile("day11.txt", i);
