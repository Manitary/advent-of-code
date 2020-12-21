//incomplete
F:=Open("input20.txt","r");

tile:=AssociativeArray();
list:=[];
grids:=[];

while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	if "T" in s then
		_, n:=Regexp("[0-9]+",s);
		Append(~list,StringToInteger(n));
		Append(~grids,[]);
	elif #s gt 0 then
		Append(~grids[#grids],s);
	end if;
end while;

l:=#grids[1];
dim:=Integers()!SquareRoot(#grids);

tile:=AssociativeArray();
for i in [1..#list] do
	tile[list[i]]:=grids[i];
end for;

function show(n)
	for i in [1..#tile[n]] do
		print tile[n][i];
	end for;
	return true;
end function;

function printgrid(grid)
	for i in [1..l] do
		if Type(grid[i]) eq MonStgElt then
			print grid[i];
		else
			print &*grid[i];
		end if;
	end for;
	return true;
end function;

function rotate(grid,i)
	if i eq 1 then
		return [[grid[a,b]:a in [l..1 by -1]]:b in [1..l]];
	elif i gt 1 then
		return rotate(rotate(grid,i-1),1);
	end if;
end function;

function flip(grid)
	return [Reverse(r):r in grid];
end function;

function allimages(grid)
	list:=[];
	for i in [1..4] do
		Append(~list,rotate(grid,i));
		Append(~list,flip(rotate(grid,i)));
		Append(~list,rotate(flip(grid),i));
	end for;
	return list;
end function;

allgrids:=[allimages(grid):grid in grids];

function borders(grid);
	return [[grid[1,i]:i in [1..l]], [grid[i,l]:i in [1..l]], [grid[l,i]:i in [1..l]], [grid[i,1]:i in [1..l]]];
end function;

procedure findpic(allgrids, ~order, ~seen, ~x, ~y, ~found)
	if x gt dim then
		x:=1;
		y+:=1;
	end if;
	if y le dim then
		if not found then
			for g in [1..#allgrids] do
				if g notin seen then
					//"test:",g," - ",x,y,seen;
					for gr in [1..#allgrids[g]] do
						matchgr:=true;
						if x gt 1 then
							if borders(order[<x-1,y>][3])[2] ne borders(allgrids[g,gr])[4] then
								matchgr:=false;
							end if;
						end if;
						if y gt 1 then
							if borders(order[<x,y-1>][3])[3] ne borders(allgrids[g,gr])[1] then
								matchgr:=false;
							end if;
						end if;
						if matchgr then
							//"found:", g, gr;
							Append(~seen,g);
							order[<x,y>]:=[*g,gr,allgrids[g,gr]*];
							x+:=1;
							findpic(allgrids,~order,~seen,~x,~y,~found);
						end if;
					end for;
				end if;
			end for;
			Remove(~order,<x,y>);
			Prune(~seen);
			x-:=1;
			if x eq 0 then
				x:=dim;
				y-:=1;
			end if;
		end if;
	else
		found:=true;
	end if;
end procedure;

order:=AssociativeArray();
seen:=[];
found:=false;
x:=1;
y:=1;
findpic(allgrids, ~order, ~seen, ~x, ~y, ~found);
