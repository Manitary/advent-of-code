F:=Open("input7.txt","r");
bags:={@@};
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	_, _, bag:=Regexp("([a-z ]+) bags? c", s);
	Include(~bags,bag[1]);
end while;

F:=Open("input7.txt","r");
G:=MultiDigraph<bags|>;
i:=0;
while true do
	i+:=1;
	s:=Gets(F);
	if IsEof(s) then
		break;	
	end if;
	bool, int:=Regexp("[0-9]",s);
	if bool then
		pos:=Index(s,int);
		contained:=Split(Substring(s,pos,#s-pos+1),",");
		for item in contained do
			_, q:=Regexp("[0-9]+",item);
			_, _, b:=Regexp("[0-9] ([a-z ]+) bag",item);
			b:=b[1];
			AddEdge(~G,V.i,V!b,StringToInteger(q));
		end for;
	end if;
end while;

V:=VertexSet(G);
target:= "shiny gold";

PrintFile("day07.txt",#{v:v in V|Reachable(v,V!target)}-1);

function FindBags(u)
	if #OutNeighbours(u) eq 0 then
		return 1;
	else
		return 1+&+[Labels(Edges(u,v))[1]*FindBags(v):v in OutNeighbours(u)];
	end if;
end function;

PrintFile("day07.txt",FindBags(V!target)-1);
