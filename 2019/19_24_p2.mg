F:=Open("input24.txt","r");
input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~input,Eltseq(s));
end while;

function mid(size)
	return Ceiling(size/2);
end function;

function EmptyBoard(size)
	return [[i eq mid(size) and j eq mid(size) select "?" else ".":j in [1..size]]:i in [1..size]];
end function;

function GetCoordsNGBH(row,col,depth,size)
	ngbh:={};
	for i in [-1..1], j in [-1..1] do
		if Abs(i)+Abs(j) eq 1 then
			if row+i eq 0 or row+i gt size then
				Include(~ngbh,<depth-1,mid(size)+i,mid(size)>);
			elif col+j eq 0 or col+j gt size then
				Include(~ngbh,<depth-1,mid(size),mid(size)+j>);
			elif row+i eq mid(size) and col eq mid(size) then
				ngbh join:={<depth+1,i eq 1 select 1 else size,k>:k in [1..size]};
			elif col+j eq mid(size) and row eq mid(size) then
				ngbh join:={<depth+1,k,j eq 1 select 1 else size>:k in [1..size]};
			else
				Include(~ngbh,<depth,row+i,col+j>);
			end if;
		end if;
	end for;
	return ngbh;
end function;

function UpdateTile(boards,r,c,d,size)
	ngbh_bugs:=0;
	ngbh_tiles:=GetCoordsNGBH(r,c,d,size);
	for tile in ngbh_tiles do
		if tile[1] gt 0 and tile[1] le #boards then
			if boards[tile[1],tile[2],tile[3]] eq "#" then
				ngbh_bugs+:=1;
			end if;
		end if;
	end for;
	if boards[d,r,c] eq "#" and ngbh_bugs ne 1 then
		return ".";
	elif boards[d,r,c] eq "." and ngbh_bugs in {1,2} then
		return "#";
	else
		return boards[d,r,c];
	end if;
end function;

function UpdateBoards(boards,size)
	new_boards:=[];
	for d in [1..#boards] do
		Append(~new_boards,[]);
		for r in [1..size] do
			Append(~new_boards[d],[]);
			for c in [1..size] do
				new_boards[d,r,c]:=UpdateTile(boards,r,c,d,size);
			end for;
		end for;
	end for;
	if new_boards[1] ne EmptyBoard(size) then
		Insert(~new_boards,1,EmptyBoard(size));
	end if;
	if new_boards[#new_boards] ne EmptyBoard(size) then
		Append(~new_boards,EmptyBoard(size));
	end if;
	return new_boards;
end function;

n:=5;
input[mid(n),mid(n)]:="?";
state:=input;
boards:=[EmptyBoard(n),state,EmptyBoard(n)];

for i in [1..200] do
	boards:=UpdateBoards(boards,n);
end for;

bugs:=0;
for d in [1..#boards], r in [1..n], c in [1..n] do
	if boards[d,r,c] eq "#" then
		bugs+:=1;
	end if;
end for;
