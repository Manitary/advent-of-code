F:=Open("input24.txt","r");

input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~input,s);
end while;

function coords(road)
	pos:=[0,0];
	i:=1;
	while i le #road do
		case road[i]:
			when "e":
				pos[1]+:=1;
			when "w":
				pos[1]-:=1;
			when "n":
				pos[2]+:=1;
				i+:=1;
				if road[i] eq "w" then
					pos[1]-:=1;
				end if;
			when "s":
				pos[2]-:=1;
				i+:=1;
				if road[i] eq "e" then
					pos[1]+:=1;
				end if;
		end case;
		i+:=1;
	end while;
	return pos;
end function;

black:={};
for pattern in input do
	tile:=coords(pattern);
	if tile in black then
		Exclude(~black, tile);
	else
		Include(~black, tile);
	end if;
end for;
PrintFile("day24.txt",#black);

function ngbh(coord)
	list:={[coord[1]+i,coord[2]+j]:i,j in [-1..1]|i*j ne 1 and not (i eq 0 and j eq 0)};
	return list;
end function;

function evolve(tiles)
	new:=tiles;
	whitengbh:=AssociativeArray();
	for t in tiles do
		tngbh:=ngbh(t);
		count:=0;
		for u in tngbh do
			count+:=u in tiles select 1 else 0;
			if u notin tiles then
				if IsDefined(whitengbh,u) then
					whitengbh[u] join:= {t};
				else
					whitengbh[u] := {t};
				end if;
			end if;
		end for;
		if count in {0} join {3..6} then
			Exclude(~new,t);
		end if;
	end for;
	for t in Keys(whitengbh) do
		if #whitengbh[t] eq 2 then
			Include(~new,t);
		end if;
	end for;
	return new;
end function;

for i in [1..100] do
	black:=evolve(black);
end for;
PrintFile("day24.txt",#black);
