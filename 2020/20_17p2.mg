F:=Open("input17.txt","r");

input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~input,Eltseq(s));
end while;

function Initialize(input);
	grid:=AssociativeArray();
	grid[<0,0>]:=AssociativeArray();
	for i,j in [1..#input] do
		grid[<0,0>][<i,j>]:=input[i,j];
	end for;
	return grid;
end function;

function ngbh(grid, x, y, z, w)
	count:=0;
	for i in [x-1..x+1], j in [y-1..y+1], k in [z-1..z+1], l in [w-1..w+1] do
		if IsDefined(grid,<k,l>) then
			if IsDefined(grid[<k,l>],<i,j>) then
				if grid[<k,l>][<i,j>] eq "#" then
					if i eq x and j eq y and k eq z and l eq w then
						continue;
					else
						count+:=1;
					end if;
				end if;
			end if;
		end if;
	end for;
	return count;
end function;

procedure Fill(~grid)
	all:=Keys(grid);
	z1:=Min({c[1]:c in all});
	z2:=Max({c[1]:c in all});
	w1:=Min({c[2]:c in all});
	w2:=Max({c[2]:c in all});
	k:=&join{Keys(grid[l]):l in all};
	x1:=Min({c[1]:c in k});
	x2:=Max({c[1]:c in k});
	y1:=Min({c[2]:c in k});
	y2:=Max({c[2]:c in k});
	for z in [z1..z2], w in [w1..w2] do
		if not IsDefined(grid,<z,w>) then
			grid[<z,w>]:=AssociativeArray();
		end if;
		for x in [x1..x2], y in [y1..y2] do
			if not IsDefined(grid[<z,w>],<x,y>) then
				grid[<z,w>][<x,y>]:=".";
			end if;
		end for;
	end for;
end procedure;

procedure Evolve(~grid)
	new:=grid;
	all:=Keys(grid);
	z1:=Min({c[1]:c in all});
	z2:=Max({c[1]:c in all});
	w1:=Min({c[2]:c in all});
	w2:=Max({c[2]:c in all});
	a:=(&join{{c[1]:c in Keys(grid[l])}:l in all});
	x1:=Min(a);
	x2:=Max(a);
	b:=(&join{{c[2]:c in Keys(grid[l])}:l in all});
	y1:=Min(b);
	y2:=Max(b);
	for x in [x1-1..x2+1], y in [y1-1..y2+1], z in [z1-1..z2+1], w in [w1-1..w2+1] do
		count:=ngbh(grid,x,y,z,w);
		if IsDefined(grid,<z,w>) then
			if IsDefined(grid[<z,w>],<x,y>) and grid[<z,w>][<x,y>] eq "#" then
				if count notin {2,3} then
					new[<z,w>][<x,y>]:=".";
				end if;
			else
				if count eq 3 then
					new[<z,w>][<x,y>]:="#";
				end if;
			end if;
		else
			if count eq 3 then
				if not IsDefined(new,<z,w>) then
					new[<z,w>]:=AssociativeArray();
				end if;
				new[<z,w>][<x,y>]:="#";
				end if;
		end if;
	end for;
	Fill(~new);
	grid:=new;
end procedure;

function Active(grid)
	count:=0;
	for k in Keys(grid) do
		for k1 in Keys(grid[k]) do
			if grid[k][k1] eq "#" then
				count+:=1;
			end if;
		end for;
	end for;
	return count;
end function;

grid:=Initialize(input);
for i in [1..6] do
	print i;
	Evolve(~grid);
end for;
Active(grid);
