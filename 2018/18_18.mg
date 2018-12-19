F:=Open("input18.txt","r");

area:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~area,Eltseq(s));
end while;

area;

function convert(grid,x,y)
	yr:=#grid;
	xr:=#grid[1];
	ngbh:={*grid[a,b]:b in [Max(1,x-1)..Min(xr,x+1)],a in [Max(1,y-1)..Min(yr,y+1)]|a ne y or b ne x*};
	if grid[y,x] eq "." then
		if Multiplicity(ngbh,"|") ge 3 then
			return "|";
		else
			return ".";
		end if;
	elif grid[y,x] eq "|" then
		if Multiplicity(ngbh,"#") ge 3 then
			return "#";
		else
			return "|";
		end if;
	elif grid[y,x] eq "#" then
		if "|" in ngbh and "#" in ngbh then
			return "#";
		else
			return ".";
		end if;
	end if;
	return false;
end function;

function evolve(grid)
	return [[convert(grid,x,y):x in [1..#grid[1]]]:y in [1..#grid]];
end function;

function display(grid)
	for i in [1..#grid] do
		print &*grid[i];
	end for;
	return true;
end function;

function value(grid)
	w:=0;
	l:=0;
	for i in [1..#grid[1]], j in [1..#grid] do
		if grid[i,j] eq "|" then
			w+:=1;
		end if;
		if grid[i,j] eq "#" then
			l+:=1;
		end if;
	end for;
	return l*w;
end function;

/*
for i in [1..10] do
	area:=evolve(area);
end for;
value(area);
*/

patterns:=[];
stored_values:=[];

n:=10^9;

for k in [1..n] do
	area:=evolve(area);
	if k eq 10 then
		value(area);
	end if;
	if area notin patterns then
		Append(~patterns,area);
	else
		first:=Index(patterns,area);
		l:=k-first;
		break;
	end if;
end for;

num_loops:=(n-first+1) div l;
last:=n-first+1-l*num_loops;
value(patterns[first+last-1]);

