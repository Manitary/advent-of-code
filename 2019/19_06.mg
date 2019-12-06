F:=Open("input6.txt","r");

G:=EmptyGraph(0);
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	obj:=Split(s,")");
	for o in obj do
		if o notin Labels(VertexSet(G)) then
			AddVertex(~G,o);
		end if;
	end for;
	G+:={VertexSet(G).Index(Labels(VertexSet(G)),obj[1]),VertexSet(G).Index(Labels(VertexSet(G)),obj[2])};
end while;

V:=VertexSet(G);
COM:=V.Index(Labels(V),"COM");
PrintFile("day06.txt",&+[Distance(COM,v):v in V]);

YOU:=V.Index(Labels(V),"YOU");
SAN:=V.Index(Labels(V),"SAN");
PrintFile("day06.txt",Distance(Geodesic(YOU,COM)[2],Geodesic(SAN,COM)[2]));
