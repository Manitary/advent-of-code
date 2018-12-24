F:=Open("input22.txt","r");
_,d:=Regexp("([0-9]+)",Gets(F));
_,_,t:=Regexp("([0-9]+),([0-9]+)",Gets(F));
depth:=StringToInteger(d);
t:=[StringToInteger(c)+1:c in t];
target:=<t[1],t[2],"T">;

forward compute_erosion;

procedure compute_index(~index,~erosion,x,y)
	while not(IsDefined(index,y)) do
		Append(~index,[]);
	end while;
	if not(IsDefined(index[y],x)) then
		if x eq 1 and y eq 1 then
			index[y,x]:=0;
		elif x eq 1 then
			index[y,x]:=(y-1)*48271;
		elif y eq 1 then
			index[y,x]:=(x-1)*16807;
		elif [x,y] eq t then
			index[y,x]:=0;
		else
			compute_erosion(~index,~erosion,x-1,y);
			compute_erosion(~index,~erosion,x,y-1);
			index[y,x]:=erosion[y,x-1]*erosion[y-1,x];
		end if;
	end if;
end procedure;

procedure compute_erosion(~index,~erosion,x,y)
	while not(IsDefined(erosion,y)) do
		Append(~erosion,[]);
	end while;
	if not(IsDefined(erosion[y],x)) then
		compute_index(~index,~erosion,x,y);
		erosion[y,x]:=(index[y,x]+depth) mod 20183;
	end if;
end procedure;

risk:=func<el|el mod 3>;
symbol:=func<r|r eq 0 select "." else (r eq 1 select "=" else "|")>;
function map(erosion)
	cc:=[[[x,y] eq [1,1] select "M" else ([x,y] eq t select "T" else symbol(risk(erosion[y,x]))):x in [1..#erosion[y]]]:y in [1..#erosion]];
	for i in [1..#cc] do
		&*cc[i];
	end for;
	return true;
end function;


erosion:=[];
index:=[];

for x in [1..t[1]], y in [1..t[2]] do
	compute_erosion(~index,~erosion,x,y);
end for;
sol:=&+{*risk(erosion[y,x]):x in [1..t[1]],y in [1..t[2]]|[x,y] ne [1,1] and [x,y] ne t*};
//PrintFile("day22.txt",sol);

tools:=func<r|r eq 0 select {"T","CG"} else (r eq 1 select {"CG","N"} else {"T","N"})>;

procedure explore(~index,~erosion,~visited,~last,~nodes)
	x:=last[1,1];
	y:=last[1,2];
	t:=last[1,3];
	ngbh:={<<x,y,Representative(Exclude(tools(risk(erosion[y,x])),t))>,7>};
	for i in [-1..1], j in [-1..1] do
		if Abs(i+j) eq 1 and y+j gt 0 and x+i gt 0 then
			compute_erosion(~index,~erosion,x+i,y+j);
			if t in tools(risk(erosion[y+j,x+i])) then
				Include(~ngbh,<<x+i,y+j,t>,1>);
			end if;
		end if;
	end for;
	for v in ngbh do
		if v[1] notin visited then
			if v[1] in Keys(nodes) then
				nodes[v[1]]:=Min(nodes[v[1]],nodes[last[1]]+v[2]);
			else
				nodes[v[1]]:=nodes[last[1]]+v[2];
				Append(~last,v[1]);
			end if;
		end if;
	end for;
	Include(~visited,last[1]);
	Remove(~nodes,last[1]);
	Remove(~last,1);
	Sort(~last,func<a,b|nodes[a]-nodes[b]>);
end procedure;

visited:={};
last:=[<1,1,"T">];
nodes:=AssociativeArray();
nodes[<1,1,"T">]:=0;

repeat
	explore(~index,~erosion,~visited,~last,~nodes);
until last[1] eq target;

PrintFile("day22.txt",nodes[target]);
