F:=Open("input13.txt","r");
text_dir:=["v","<",">","^"];
dir:=[Vector(v):v in [[1,0],[0,-1],[0,1],[-1,0]]];
m:=map<text_dir->dir|x:->dir[Index(text_dir,x)]>;

grid:=[[]];
carts:=[];
orientations:=[];
while true do
	s:=Getc(F);
	if IsEof(s) then
		break;
	end if;
	if StringToCode(s) eq 10 then
		Append(~grid,[]);
	elif StringToCode(s) notin {10,13} then
		Append(~grid[#grid],s);
		if s in text_dir then
			Append(~carts,[#grid,#grid[#grid]]);
			Append(~orientations,<m(s),GF(3)!0>);
			grid[#grid][#grid[#grid]]:=s in {"v","^"} select "|" else "-";
		end if;
	end if;
end while;

procedure move(grid,~coord,~direction,~turns)
	coord[1]+:=direction[1];
	coord[2]+:=direction[2];
	case grid[coord[1],coord[2]]:
		when "/": direction*:=Matrix([[0,-1],[-1,0]]);
		when "\\": direction*:=Matrix([[0,1],[1,0]]);
		when "+":
			case turns:
				when 0: direction*:=Matrix([[0,1],[-1,0]]);
				when 2: direction*:=Matrix([[0,-1],[1,0]]);
			end case;
			turns+:=1;
	end case;
end procedure;

procedure move_all(grid,~carts,~directions,~collisions)
	i:=0;
	while i lt #carts do
		i+:=1;
		move(grid,~carts[i],~directions[i][1],~directions[i][2]);
		new_coords:=carts[i];
		if Multiplicity(carts,new_coords) gt 1 then
			Append(~collisions,new_coords);
			i-:=Index(carts,new_coords) lt i select 2 else 1;
			while new_coords in carts do
				Remove(~directions,Index(carts,new_coords));
				Exclude(~carts,new_coords);
			end while;
		end if;
	end while;
	ParallelSort(~carts,~directions);
end procedure;

carts1:=carts;
orientations1:=orientations;
collisions:=[];

repeat
	move_all(grid,~carts1,~orientations1,~collisions);
until #collisions gt 0;

PrintFile("day13.txt",Sprintf("%o,%o",collisions[1][2]-1,collisions[1][1]-1));

carts1:=carts;
orientations1:=orientations;
collisions:=[];

repeat
	move_all(grid,~carts,~orientations,~collisions);
until #carts eq 1;

PrintFile("day13.txt",Sprintf("%o,%o",carts[1][2]-1,carts[1][1]-1));
