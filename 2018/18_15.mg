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

units:=[];
ap:=3;
hp:=200;

for i in [1..h], j in [1..w] do
	if grid[i,j] ne "#" then
		if grid[i,j] ne "." then
			Append(~units,<[i,j],grid[i,j],hp,ap>);
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

units:=[<m(u[1]),u[2],u[3],u[4]>:u in units];

procedure move(~unit,units);
	dist:=[];
	if #(Neighbours(unit[1]) meet {u[1]:u in units|u[2] ne unit[2]}) eq 0 then
		for u in [u:u in units|u ne unit and u[2] ne unit[2]] do
			H,W,F:=sub<G|{v:v in V|v notin [c[1]:c in units|c ne u and c ne unit]}>;
			s:=W!unit[1];
			f:=W!u[1];
			if Reachable(s,f) then
				d:=Distance(s,f);
				ngbh:=Sort([v:v in Neighbours(f)|Reachable(s,v) and Distance(s,v) eq d-1])[1];
				Append(~dist,<d-1,ngbh>);
			end if;
		end for;
		if #dist gt 0 then
			close:=Sort([d:d in dist|d[1] eq Min([c[1]:c in dist])])[1];
			W:=Parent(close[2]);
			s:=W!unit[1];
			tile:=Sort([x:x in Neighbours(s)|Reachable(x,close[2]) and Distance(x,close[2]) eq close[1]-1])[1];
			unit[1]:=V!tile;
		end if;
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

/*
win:=false;
t:=0;
repeat
	play_round(~units,~win,~t);
	show_grid(units);
until win;
*/

elf:=#{u:u in units|u[2] eq "E"};
old_units:=units;
elf_atk:=ap;

while true do
	"NEW GAME STARTING";
	elf_atk;
	units:=[<u[1],u[2],u[3],u[2] eq "E" select elf_atk else ap>:u in old_units];
	win:=false;
	t:=0;
	repeat
		play_round(~units,~win,~t);
		show_grid(units);
		if #{u:u in units|u[2] eq "E"} lt elf then
			break;
		end if;
	until win;
	if win then
		break;
	end if;
	elf_atk+:=1;
end while;

t;
show_grid(units);
t*&+{*c[3]:c in units*};
