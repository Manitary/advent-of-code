F:=Open("input8.txt","r");
s:=[StringToInteger(c):c in Split(Gets(F)," ")];

i:=3;
parents:=[s[1]];
meta:=[s[2]];
G:=EmptyDigraph(1);
node:=1;
labels:=[];

while i le #s do
	if parents[#parents] eq 0 then
		labels[node]:=[s[i+j]:j in [0..meta[#meta]-1]];
		i+:=meta[#meta];
		Prune(~meta);
		Prune(~parents);
		repeat
			node-:=1;
		until node eq 0 or not(IsDefined(labels,node));
	else
		parents[#parents]-:=1;
		G+:=1;
		G+:=[VertexSet(G).node,VertexSet(G).(#VertexSet(G))];
		node:=#VertexSet(G);
		Append(~parents,s[i]);
		Append(~meta,s[i+1]);		
		i+:=2;
	end if;
end while;

PrintFile("day08.txt",&+[&+l:l in labels]);

function value(node)
	ngbh:=Sort([Index(v):v in OutNeighbours(VertexSet(G).node)]);
	if #ngbh eq 0 then
		return &+labels[node];
	else
		return &+[IsDefined(ngbh,l) select value(ngbh[l]) else 0:l in labels[node]];
	end if;
end function;

PrintFile("day08.txt",value(1));
