F:=Open("input20.txt","r");
dir:={"N","S","W","E"};

procedure travel(~graph,~curr,~branch,~nodes,~done)
	char:=Getc(F);
	n:=NumberOfVertices(graph);
	if char in dir then
		case char:
			when "N": new:=curr+Vector([0,1]);
			when "E": new:=curr+Vector([1,0]);
			when "S": new:=curr+Vector([0,-1]);
			when "W": new:=curr+Vector([-1,0]);
		end case;
		if new notin Keys(nodes) then
			nodes[new]:=n+1;
			graph:=(graph+1);
		end if;
		graph+:={{nodes[curr],nodes[new]}};
		curr:=new;
	elif char eq "(" then
		Append(~branch,curr);
	elif char eq "|" then
		curr:=branch[#branch];
	elif char eq ")" then
		curr:=branch[#branch];
		Prune(~branch);
	elif char eq "$" then
		done:=true;
	end if;
end procedure;

G:=EmptyGraph(1);
nodes:=AssociativeArray();
curr:=Vector([0,0]);
nodes[curr]:=1;
branch:=[];
done:=false;

repeat
	travel(~G,~curr,~branch,~nodes,~done);
until done;

visited:={};
last:={VertexSet(G).1};
i:=0;
repeat
	i+:=1;
	new:=&join{Neighbours(v):v in last};
	visited join:=last;
	last:=new diff visited;
until #last eq 0;
PrintFile("day20.txt",i-1);

d:=1000;
PrintFile("day20.txt",NumberOfVertices(G)-#Ball(VertexSet(G).1,d-1));
