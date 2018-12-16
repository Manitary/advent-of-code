F:=Open("input15.txt","r");

grid:=[];

while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~grid,Eltseq(s));
end while;

w:=#grid[1];
h:=#grid;

cunt:=func<n,m|n mod m eq 0 select [n div m,m] else [n div m+1,n mod m]>;

G:=EmptyGraph(h*w);
V:=VertexSet(G);
m:=map<[[i,j]:i in [1..h],j in [1..w]]->V|x:->VertexSet(G).(w*(x[1]-1)+x[2]),y:->cunt(Index(y),w)>;

base_units:=[];
ap:=3;
hp:=200;

for i in [1..h], j in [1..w] do
	if grid[i,j] ne "#" then
		if grid[i,j] ne "." then
			Append(~base_units,<[i,j],grid[i,j],hp,ap>);
			grid[i,j]:=".";
		end if;
		if grid[i,j+1] ne "#" then
			G+:={m([i,j]),m([i,j+1])};
		end if;
		if grid[i+1,j] ne "#" then
			G+:={m([i,j]),m([i+1,j])};
		end if;
	end if;
end for;

V:=VertexSet(G);
m:=map<[[i,j]:i in [1..h],j in [1..w]]->V|x:->VertexSet(G).(w*(x[1]-1)+x[2]),y:->cunt(Index(y),w)>;
E:=EdgeSet(G);

base_units:=[<m(u[1]),u[2],u[3],u[4]>:u in base_units];

procedure move(~unit,units);
	dist:=[];
	if #(Neighbours(unit[1]) meet {u[1]:u in units|u[2] ne unit[2]}) eq 0 then
		H,W:=sub<G|{v:v in V|v notin [c[1]:c in units|c ne unit and c[2] eq unit[2]]}>;
		opp:={W!c[1]:c in units|c[2] ne unit[2]};
		targets:=&join{Neighbours(o):o in opp};
		s:=W!unit[1];
		r:=0;
		while true do
			r+:=1;
			b:=Sphere(s,r);
			if #b eq 0 then
				break;
			end if;
			close:=targets meet b;
			if #close gt 0 then
				close:=Sort(SetToSequence(close))[1];
				tile:=Sort([x:x in Neighbours(s)|close in Sphere(x,r-1)])[1];
				unit[1]:=V!tile;
				break;
			end if;
		end while;
	end if;
end procedure;

procedure attack(~units,atk,~i,~win)
	def:=[u:u in units|u[1] in Neighbours(atk[1]) and u[2] ne atk[2]];
	if #def gt 0 then
		def:=[u:u in def|u[3] eq Min({u[3]:u in def})];
		idx:=Index(units,Sort(def)[1]);
		units[idx][3]-:=atk[4];
		if units[idx][3] le 0 then
			if idx lt Index(units,atk) then
				i-:=1;
			end if;
			Remove(~units,idx);
			if #{u[2]:u in units} eq 1 then
				win:=true;
			end if;
		end if;
	end if;
end procedure;

procedure play_round(~units,~win,~t)
	i:=0;
	while i lt #units do
		i+:=1;
		move(~units[i],units);
		attack(~units,units[i],~i,~win);
		if win then
			break;
		end if;
	end while;
	Sort(~units);
	if not(win) or (win and i eq #units) then
		t+:=1;
	end if;
end procedure;

function show_grid(units)
	cc:=grid;
	for u in units do
		cc[(u[1]@@m)[1],(u[1]@@m)[2]]:=u[2];
	end for;
	return cc;
end function;

function print_turn(units,t,filename)
	cc:=grid;
	for u in units do
		cc[(u[1]@@m)[1],(u[1]@@m)[2]]:=u[2];
	end for;
	PrintFile(filename,"Round: " cat IntegerToString(t));
	PrintFile(filename,"Units: ");
	PrintFile(filename,[<u[1]@@m,u[2],u[3],u[4]>:u in units]);
	for i in [1..#cc] do
		PrintFile(filename,&*cc[i]);
	end for;
	PrintFile(filename,"");
	return true;
end function;

function outcome(units,t)
	return t*&+{*c[3]:c in units*};
end function;


units:=base_units;
win:=false;
t:=0;
repeat
	play_round(~units,~win,~t);
until win;
PrintFile("day15.txt",outcome(units,t));

elf:=#{u:u in base_units|u[2] eq "E"};
elf_atk:=ap;
while true do
	units:=[<u[1],u[2],u[3],u[2] eq "E" select elf_atk else ap>:u in base_units];
	win:=false;
	t:=0;
	repeat
		play_round(~units,~win,~t);
		if #{u:u in units|u[2] eq "E"} lt elf then
			break;
		end if;
	until win;
	if win then
		break;
	end if;
	elf_atk+:=1;
end while;
PrintFile("day15.txt",outcome(units,t));
