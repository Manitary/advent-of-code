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
	grid:=AssociativeArray(Integers());
	grid[0]:=AssociativeArray();
	for i,j in [1..#input] do
		grid[0][<i,j>]:=input[i,j];
	end for;
	return grid;
end function;

function ngbh(grid, x, y, z)
	count:=0;
	for i in [x-1..x+1], j in [y-1..y+1], k in [z-1..z+1] do
		if IsDefined(grid,k) then
			if IsDefined(grid[k],<i,j>) then
				if grid[k][<i,j>] eq "#" then
					if i eq x and j eq y and k eq z then
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
	k:=&join{Keys(grid[l]):l in Keys(grid)};
	x1:=Min({c[1]:c in k});
	x2:=Max({c[1]:c in k});
	y1:=Min({c[2]:c in k});
	y2:=Max({c[2]:c in k});
	for z in Keys(grid) do
		for x in [x1..x2], y in [y1..y2] do
			if not IsDefined(grid[z],<x,y>) then
				grid[z][<x,y>]:=".";
			end if;
		end for;
	end for;
	//return true;
end procedure;

procedure Print(grid)
	for z in Sort(SetToSequence(Keys(grid))) do
		k:=Keys(grid[z]);
		x1:=Min({c[1]:c in k});
		x2:=Max({c[1]:c in k});
		y1:=Min({c[2]:c in k});
		y2:=Max({c[2]:c in k});
		for x in [x1..x2] do
			print Explode([grid[z][<x,y>]:y in [y1..y2]]);
		end for;
		print "-";
	end for;
	//return true;
end procedure;

procedure Evolve(~grid)
	new:=grid;
	k:=Keys(grid);
	z1:=Min(k);
	z2:=Max(k);
	a:=(&join{{c[1]:c in Keys(grid[l])}:l in k});
	x1:=Min(a);
	x2:=Max(a);
	b:=(&join{{c[2]:c in Keys(grid[l])}:l in k});
	y1:=Min(b);
	y2:=Max(b);
	for x in [x1-1..x2+1], y in [y1-1..y2+1], z in [z1-1..z2+1] do
		count:=ngbh(grid,x,y,z);
		if IsDefined(grid,z) then
			if IsDefined(grid[z],<x,y>) and grid[z][<x,y>] eq "#" then
				if count notin {2,3} then
					new[z][<x,y>]:=".";
				end if;
			else
				if count eq 3 then
					new[z][<x,y>]:="#";
				end if;
			end if;
		else
			if count eq 3 then
				if not IsDefined(new,z) then
					new[z]:=AssociativeArray();
				end if;
				new[z][<x,y>]:="#";
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
	Evolve(~grid);
end for;
Active(grid);
