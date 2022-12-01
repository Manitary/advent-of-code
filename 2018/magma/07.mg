F:=Open("input7.txt","r");
steps:={};

while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	_,_,c:=Regexp("Step ([A-Z]).*([A-Z])",s);
	Include(~steps,Reverse(c));
end while;

num:=func<c|StringToCode(c)-64>;
ch:=func<n|CodeToString(n+64)>;

G:=EmptyDigraph(26);
for p in steps do
	AddEdge(~G,num(p[1]),num(p[2]));
end for;

w:=[];
repeat
	for v in VertexSet(G) do
		if Index(v) notin w and OutDegree(v) eq 0 then
			Append(~w,Index(v));
			RemoveEdges(~G,IncidentEdges(v));
			break;
		end if;
	end for;
until #EdgeSet(G) eq 0;
for i in [1..26] do
	if i notin w then
		Append(~w,i);
		break;
	end if;
end for;

PrintFile("day07.txt",&*[ch(i):i in w]);

G:=EmptyDigraph(26);
for p in steps do
	AddEdge(~G,num(p[1]),num(p[2]));
end for;
AssignVertexLabels(~G,[61..86]);

word:=[];
t:=0;
w:=5;
ot:=60;
active:=[];
repeat
	available:=[Index(v):v in VertexSet(G)|Index(v) notin word and Index(v) notin active and OutDegree(v) eq 0];
	available:=[available[i]: i in [1..#available]|i le w];
	w-:=#available;
	active cat:=available;
	s:=Min([Label(VertexSet(G).v):v in active]);
	AssignLabels(~G,[VertexSet(G).v:v in active],[Label(VertexSet(G).v)-s:v in active]);
	done:=[v:v in active|Label(VertexSet(G).v) eq 0];
	active:=[v:v in active|v notin done];
	t+:=s;
	w+:=#done;
	word cat:=done;
	RemoveEdges(~G,&join{IncidentEdges(VertexSet(G).v):v in done});
until {c:c in Labels(VertexSet(G))} eq {0};

PrintFile("day07.txt",t);
