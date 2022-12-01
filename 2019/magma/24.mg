F:=Open("input24.txt","r");
input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~input,Eltseq(s));
end while;

function UpdateTile(board,r,c)
	rows:=#board;
	cols:=#board[1];
	ngbh_bugs:=0;
	for i in [-1..1], j in [-1..1] do
		if Abs(i)+Abs(j) eq 1 and r+i ge 1 and c+j ge 1 and r+i le rows and c+j le cols then
			ngbh_bugs+:=board[r+i,c+j] eq "#" select 1 else 0;
		end if;
	end for;
	if board[r,c] eq "#" and ngbh_bugs ne 1 then
		return ".";
	elif board[r,c] eq "." and ngbh_bugs in {1,2} then
		return "#";
	else
		return board[r,c];
	end if;
end function;

function UpdateBoard(board)
	new_board:=[];
	for r in [1..#board] do
		Append(~new_board,[]);
		for c in [1..#board[1]] do
			new_board[r,c]:=UpdateTile(board,r,c);
		end for;
	end for;
	return new_board;
end function;

function ComputeScore(board)
	score:=0;
	i:=-1;
	for r in [1..#board], c in [1..#board[1]] do
		i+:=1;
		if board[r,c] eq "#" then
			score+:=2^i;
		end if;
	end for;
	return score;
end function;

state:=input;
boards:={};

while true do
	print state;
	score:=ComputeScore(state);
	print score;
	if score in boards then
		"found";
		break;
	else
		Include(~boards,score);
	end if;
	state:=UpdateBoard(state);
end while;


