F:=Open("input23.txt","r");

G:=EmptyGraph(19);
V:=VertexSet(G);
for i in [1..10] do
	AddEdge(~G, V.i, V.(i+1));
end for;
AddEdges(~G, {{V.3,V.12},{V.12,V.13},{V.5,V.14},{V.14,V.15},{V.7,V.16},{V.16,V.17},{V.9,V.18},{V.18,V.19}});
V:=VertexSet(G);

hall:={V.1, V.2, V.4, V.6, V.8, V.10, V.11};
rooms:={V.i:i in [12..19]};
goal:=[[V.(11+2*(j-1)+i):i in [1..2]]:j in [1..4]];
energy:=[1,10,100,1000];

animals:=[<1,V.14>,<1,V.15>,<2,V.17>,<2,V.19>,<3,V.13>,<3,V.18>,<4,V.12>,<4,V.16>];

function CheckSol(currpos)
	return &and{x[2] in goal[x[1]]:x in currpos};
end function;

function ListMoves(currpos)
	moves:=[];
	for a in currpos do
		if a[2] notin goal[a[1]] then
			free:={x:x in V};
			for b in currpos do
				if b ne a then
					Exclude(~free, b[2]);
				end if;
			end for;
			dest:=SequenceToSet(goal[a[1]]) meet free;
			if #dest eq 2 then
				dest:=goal[a[1],2];
			elif #dest eq 1 then
				if not exists(x){c:c in currpos|c[1] eq a[1] and c ne a and c[2] eq goal[a[1],2]} then
					dest:={};
				end if;
			end if;
			if #dest eq 0 then
				dest:=a[2] in rooms select hall meet free else {};
			end if;
			H:=sub<G|free>;
			W:=VertexSet(H);
			for w in dest do
				if Reachable(W!a[2],W!w) then
					Append(~moves, <Distance(W!a[2],W!w)*energy[a[1]], a, w>);
				end if;
			end for;
		end if;
	end for;
	return Sort(moves);
end function;

function Move(currpos, cost)
	if CheckSol(currpos) then
		return cost;
	end if;
	moves:=ListMoves(currpos);
	if #moves eq 0 then
		return false;
	end if;
	for move in moves do
		if Move(currpos,cost+move[1]) then
			return cost+move[1];
		end if;
	end for;
	return false;
end function;

Move(animals,0);

//rip segfault