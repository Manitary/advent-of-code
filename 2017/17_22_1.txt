input:=["..####.###.##..##....##..",".##..#.###.##.##.###.###.","......#..#.#.....#.....#.","##.###.#.###.##.#.#..###.","#..##...#.....##.#..###.#",".#..#...####...#.....###.","##...######.#.###..#.##..","###..#..##.###....##.....",".#.#####.###.#..#.#.#..#.","#.#.##.#.##..#.##..#....#","..#.#.#.#.#.##...#.####..","##.##..##...#..##..#.####","#.#..####.##.....####.##.","..####..#.#.#.#.##..###.#","..#.#.#.###...#.##..###..","#.####.##..###.#####.##..",".###.##...#.#.#.##....#.#","#...######...#####.###.#.","#.####.#.#..#...##.###...","####.#.....###..###..#.#.","..#.##.####.#######.###..","#.##.##.#.#.....#...#...#","###.#.###..#.#...#...##..","##..###.#..#####.#..##..#","#......####.#.##.#.###.##"];

function convert(c)
	if c eq "." then
		return -1;
	elif c eq "#" then
		return 1;
	end if;
end function;

procedure burst(~grid,~position,~direction,~infections)
	for c in [1..#grid] do
		if grid[c][1] eq position[1] and grid[c][2] eq position[2] then
			direction:=RowSequence(Matrix([direction])*Matrix([[0,-grid[c][3]],[grid[c][3],0]]))[1];
			infections+:=Integers()!(-grid[c][3]/2+1/2);
			grid[c][3]*:=-1;
			position+:=direction;
			break;
		else
			Append(~grid,Append(position,-1));
			burst(~grid,~position,~direction,~infections);
			break;
		end if;
	end for;
end procedure;

grid:=[];
r:=Integers()!((#input-1)/2);
for x in [-r..r] do
	for y in [-r..r] do
		Append(~grid,[x,y,convert(input[-y+r+1][x+r+1])]);
	end for;
end for;
position:=[0,0];
direction:=[0,1];
infections:=0;

for i in [1..10000] do
	burst(~grid,~position,~direction,~infections);
end for;
infections;