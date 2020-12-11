F:=Open("input11.txt","r");

input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~input,Eltseq(s));
end while;
nr:=#input;
nc:=#input[1];

dir:=Exclude({Vector([x,y]):x,y in [-1..1]},Vector([0,0]));

function GetNGBH(grid, r,c)
	return #{<x,y>:x in [Max(r-1,1)..Min(r+1,nr)], y in [Max(c-1,1)..Min(c+1,nc)]|[x,y] ne [r,c] and grid[x,y] eq "#"};
end function;

function Evolve(grid)
	new:=grid;
	changed:=false;
	for r in [1..nr], c in [1..nc] do
		if grid[r,c] eq "L" then
			if GetNGBH(grid,r,c) eq 0 then
				new[r,c]:="#";
				changed:=true;
			end if;
		elif grid[r,c] eq "#" then
			if GetNGBH(grid,r,c) ge 4 then
				new[r,c]:="L";
				changed:=true;
			end if;
		end if;
	end for;
	return new, changed;
end function;

new:=input;
repeat
	new, change:=Evolve(new);
until not change;
PrintFile("day11.txt",#{[x,y]:x in [1..nr], y in [1..nc]|new[x,y] eq "#"});


function CheckSeats(grid, x, y)
	pos:=Vector([x,y]);
	count:=0;
	for d in dir do
		check:=pos;
		while true do
			check+:=d;	
			if check[1] eq 0 or check[1] gt nr or check[2] eq 0 or check[2] gt nc or grid[check[1],check[2]] eq "L" then
				break;
			elif 
				grid[check[1],check[2]] eq "#" then
				count+:=1;
				break;
			end if;
		end while;
	end for;
	return count;
end function;

function Evolve2(grid)
	new:=grid;
	changed:=false;
	for r in [1..nr], c in [1..nc] do
		if grid[r,c] eq "L" then
			if CheckSeats(grid, r, c) eq 0 then
				new[r,c]:="#";
				changed:=true;
			end if;
		elif grid[r,c] eq "#" then
			if CheckSeats(grid, r, c) ge 5 then
				new[r,c]:="L";
				changed:=true;
			end if;
		end if;
	end for;
	return new, changed;
end function;

new:=input;
repeat
	new, change:=Evolve2(new);
until not change;
PrintFile("day11.txt",#{[x,y]:x in [1..nr], y in [1..nc]|new[x,y] eq "#"});
