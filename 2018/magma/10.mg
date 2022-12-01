F:=Open("input10.txt","r");
p:=[];
v:=[];

while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	_,_,c:=Regexp("([- 0-9]+), ([- 0-9]+)> velocity=<([- 0-9]+), ([- 0-9]+)",s);
	Append(~p,[StringToInteger(c[1]),StringToInteger(c[2])]);
	Append(~v,[StringToInteger(c[3]),StringToInteger(c[4])]);
end while;

dist:=func<a,b|Abs(a[1]-b[1])+Abs(a[2]-b[2])>;

t:=0;
repeat
	t+:=1;
	for i in [1..#p], j in [1..2] do
		p[i][j]+:=v[i][j];
	end for;
	done:=true;
	for a in p do
		has_ngbh:=false;
		for b in p do
			if b ne a and dist(a,b) in {1,2} then
				has_ngbh:=true;
				break;
			end if;
		end for;
		if not(has_ngbh) then
			done:=false;
			break;
		end if;
	end for;
until done;

max_x:=Max({a[1]:a in p});
min_x:=Min({a[1]:a in p});
max_y:=Max({a[2]:a in p});
min_y:=Min({a[2]:a in p});

N:=[[".":x in [1..max_x-min_x+1]]:y in [1..max_y-min_y+1]];
for a in p do
	N[a[2]-min_y+1][a[1]-min_x+1]:="#";
end for;

PrintFile("day10.txt",N);
PrintFile("day10.txt",t);
