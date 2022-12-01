F:=Open("input3.txt","r");
wires:=[Split(Gets(F),","):w in [1,2]];

procedure Move(~curr,dir)
	case dir:
		when "R":
			curr[1]+:=1;
		when "L":
			curr[1]-:=1;
		when "U":
			curr[2]+:=1;
		when "D":
			curr[2]-:=1;
	end case;
end procedure;

procedure Execute(command,~curr,~visited)
	dir:=command[1];
	dist:=StringToInteger(Substring(command,2,#command-1));
	for i in [1..dist] do
		Move(~curr,dir);
		Append(~visited,curr);
	end for;
end procedure;

nodes:=[[]:wire in wires];
for wire in wires do
	pos:=[0,0];
	for instruction in wire do
		Execute(instruction,~pos,~nodes[Index(wires,wire)]);
	end for;
end for;

crossings:=SequenceToSet(nodes[1]) meet SequenceToSet(nodes[2]);

PrintFile("day03.txt",Min([Abs(c[1])+Abs(c[2]):c in crossings]));
PrintFile("day03.txt",Min([Index(nodes[1],c)+Index(nodes[2],c):c in crossings]));
