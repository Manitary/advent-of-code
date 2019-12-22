F:=Open("input20.txt","r");

maze:=[];
G:=EmptyGraph(0);
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~maze,Eltseq(s));
	for i in [2..#maze[#maze]] do
		if maze[#maze,i] eq "." then
			AddVertex(~G,<[#maze,i],".",0>);
			if maze[#maze,i-1] eq "." then
				G+:={VertexSet(G).NumberOfVertices(G),VertexSet(G).(NumberOfVertices(G)-1)};
			end if;
			if maze[#maze-1,i] eq "." then
				G+:={VertexSet(G).NumberOfVertices(G),VertexSet(G).Index(Labels(VertexSet(G)),<[#maze-1,i],".",0>)};
			end if;
		end if;
	end for;
end while;

not_letters:={"#","."," "};
for r in [2..#maze-1], c in [2..#maze[r]-1] do
	if maze[r,c] notin not_letters then
		V:=VertexSet(G);
		print r,c,maze[r,c];
		if maze[r-1,c] notin not_letters and maze[r+1,c] eq "." then
			AssignLabel(~G,V.Index(Labels(V),<[r+1,c],".",0>),<[r+1,c],maze[r-1,c]*maze[r,c],r eq 2 select -1 else 1>);
		elif maze[r+1,c] notin not_letters and maze[r-1,c] eq "." then
			AssignLabel(~G,V.Index(Labels(V),<[r-1,c],".",0>),<[r-1,c],maze[r,c]*maze[r+1,c],r eq #maze-1 select -1 else 1>);
		elif maze[r,c-1] notin not_letters and maze[r,c+1] eq "." then
			AssignLabel(~G,V.Index(Labels(V),<[r,c+1],".",0>),<[r,c+1],maze[r,c-1]*maze[r,c],c eq 2 select -1 else 1>);
		elif maze[r,c+1] notin not_letters and maze[r,c-1] eq "." then
			AssignLabel(~G,V.Index(Labels(V),<[r,c-1],".",0>),<[r,c-1],maze[r,c]*maze[r,c+1],c eq #maze[r]-1 select -1 else 1>);
		end if;
	end if;
end for;

G1:=G;

tp_name:={Label(v)[2]:v in VertexSet(G)} diff {"."};
for tp in tp_name do
	if exists(tp1){v:v in VertexSet(G)|Label(v)[2] eq tp} and exists(tp2){v:v in VertexSet(G)|Label(v)[2] eq tp and v ne tp1} then
		G+:={tp1,tp2};
	end if;
end for;

exists(start){v:v in VertexSet(G)|Label(v)[2] eq "AA"};
exists(finish){v:v in VertexSet(G)|Label(v)[2] eq "ZZ"};

Distance(start,finish);

V:=VertexSet(G1);
all_tp:={<Label(v)[2],Label(v)[3]>:v in V|Label(v)[2] in tp_name diff {"ZZ"}};
ngbh:=AssociativeArray(all_tp);
for tp in all_tp do
	exists(node){v:v in V|<Label(v)[2],Label(v)[3]> eq tp};
	ngbh_portals:={V!v:v in VertexSet(Component(node))|Label(V!v)[2] in tp_name};
	ngbh[tp]:={<Label(portal)[2],-Label(portal)[3],Distance(node,portal)+1>:portal in ngbh_portals|Label(portal)[2] ne "AA" and (portal ne node or Label(portal)[2] ne "ZZ")};
end for;

function GetNGBHPortals(portal,level,distance)
	return {<<p[1],p[2],level-p[2]>,distance+p[3]>:p in ngbh[portal]|(p[1] ne "ZZ" or level eq 0) and level-p[2] ge 0};
end function;

target:=<"ZZ",1,1>;
queue:=[<<"AA",-1,0>,0>];
visited:={};

while true do
	pos:=queue[1];
	print #queue;
	if pos[1,1] eq "ZZ" then
		print queue[1];
		break;
	end if;
	Include(~visited,pos[1]);
	Remove(~queue,1);
	for p in GetNGBHPortals(<pos[1,1],pos[1,2]>,pos[1,3],pos[2]) do
		if p[1] notin visited then
			Append(~queue,p);
		end if;
	end for;
	Sort(~queue,func<u,v|u[2]-v[2]>);
end while;
