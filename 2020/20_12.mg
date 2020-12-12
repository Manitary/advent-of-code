F:=Open("input12.txt","r");

input:=[];
while true do
	s:=Getc(F);
	if IsEof(s) then
		break;
	end if;
	Append(~input,[*s,StringToInteger(Gets(F))*]);
end while;

procedure move(~pos, rule, ~dir)
	case rule[1]:
		when "N":
			pos+:=Vector([0,rule[2]]);
		when "S":
			pos-:=Vector([0,rule[2]]);
		when "E":
			pos+:=Vector([rule[2],0]);
		when "W":
			pos-:=Vector([rule[2],0]);
		when "F":
			pos+:=rule[2]*dir;
		when "L":
			for i in [1..rule[2] div 90] do
				dir*:=Matrix([[0,1],[-1,0]]);
			end for;
		when "R":
			for i in [1..rule[2] div 90] do
				dir*:=Matrix([[0,-1],[1,0]]);
			end for;
	end case;
end procedure;

pos:=Vector([0,0]);
dir:=Vector([1,0]);
for r in input do
	move(~pos,r,~dir);
end for;
PrintFile("day12.txt",Abs(pos[1])+Abs(pos[2]));

procedure move2(~pos, rule, ~dir)
	case rule[1]:
		when "N":
			dir+:=Vector([0,rule[2]]);
		when "S":
			dir-:=Vector([0,rule[2]]);
		when "E":
			dir+:=Vector([rule[2],0]);
		when "W":
			dir-:=Vector([rule[2],0]);
		when "F":
			pos+:=rule[2]*dir;
		when "L":
			for i in [1..rule[2] div 90] do
				dir*:=Matrix([[0,1],[-1,0]]);
			end for;
		when "R":
			for i in [1..rule[2] div 90] do
				dir*:=Matrix([[0,-1],[1,0]]);
			end for;
	end case;
end procedure;

pos:=Vector([0,0]);
dir:=Vector([10,1]);
for r in input do
	move2(~pos,r,~dir);
end for;
PrintFile("day12.txt",Abs(pos[1])+Abs(pos[2]));
