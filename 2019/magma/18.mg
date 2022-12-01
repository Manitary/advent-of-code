F:=Open("input18.txt","r");

G:=EmptyGraph(0);
map:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~map,Eltseq(s));
end while;

for i in [2..#map-1], j in [2..#map[1]-1] do
	if map[i,j] ne "#" then
		AddVertex(~G,<[i,j],map[i,j]>);
		if exists(prev_left){v:v in VertexSet(G)|Label(v)[1] eq [i,j-1]} then
			G+:={prev_left,VertexSet(G).NumberOfVertices(G)};
		end if;
		if exists(prev_up){v:v in VertexSet(G)|Label(v)[1] eq [i-1,j]} then
			G+:={prev_up,VertexSet(G).NumberOfVertices(G)};
		end if;
	end if;
end for;

V:=VertexSet(G);
exists(origin){v:v in V|Label(v)[2] eq "@"};
points:=[v:v in V|Label(v)[2] notin {".","@"}];
Sort(~points,func<u,v|StringToCode(Label(u)[2])-StringToCode(Label(v)[2])>);
doors:=[points[i]:i in [1..26]];
keys:=[points[i]:i in [27..52]];
obstacles:=[[v:v in Geodesic(start,k)|v in doors]:k in keys];
keys_required:=[[keys[Index(doors,d)]:d in o]:o in obstacles];
letters:={Label(v)[2]:v in keys};

while exists(useless){v:v in VertexSet(G)|Degree(v) eq 1 and Label(v)[2] notin letters} do
	G-:=useless;
end while;

function PrintMap(map,graph)
	for i in [2..#map-1] do
		line:="";
		for j in [2..#map[1]-1] do
			if exists(tile){Label(v)[2]:v in VertexSet(G)|Label(v)[1] eq [i,j]} then
				line*:=tile;
			else
				line*:=" ";
			end if;
		end for;
		print line;
		//PrintFile("map.txt",line);
	end for;
end function;

path:=["@","b","w","c","f","s","n","q","W","h","j","H","o","l","r","u","O","p","Q","g","U","R","m","M","S","N","v","P","k","V","z","x","d","Z","X","D","y","t","T","i","I","a","e"];

walk:=0;
for i in [1..#path-1] do
	exists(start){v:v in VertexSet(G)|Label(v)[2] eq path[i]};
	exists(finish){v:v in VertexSet(G)|Label(v)[2] eq path[i+1]};
	walk+:=Distance(start,finish);
end for;
PrintFile("day18.txt",walk);

exists(origin){v:v in VertexSet(G)|Label(v)[2] eq "@"};
centre:=Label(origin)[1];
t:=0;
for i in [-1..1], j in [-1..1] do
	exists(node){v:v in VertexSet(G)|Label(v)[1] eq [centre[1]+i,centre[2]+j]};
	if Abs(i)+Abs(j) le 1 then
		G-:=node;
	end if;
	if Abs(i)+Abs(j) eq 2 then
		t+:=1;
		AssignLabel(node,<Label(node)[1],"@"*IntegerToString(t)>);
	end if;
end for;

paths:=[["@1","b","w","c","f","s","n","q"],["@3","W","h"],["@4","j"],["@2","H","o","l","r"],["j","u","O","p","Q","g"],["h","U","R","m"],["r","M","S","N","v"],["m","P","k","V","z","x","d"],["v","Z","X","D","y","t","T","i","I","a","e"]];

walk:=0;
for path in paths do
	for i in [1..#path-1] do
		exists(start){v:v in VertexSet(G)|Label(v)[2] eq path[i]};
		exists(finish){v:v in VertexSet(G)|Label(v)[2] eq path[i+1]};
		walk+:=Distance(start,finish);
	end for;
end for;
PrintFile("day18.txt",walk);
