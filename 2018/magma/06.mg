F:=Open("input6.txt","r");
points:=[];

while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	_,_,c:=Regexp("([0-9]+), ([0-9]+)",s);
	Append(~points,[StringToInteger(x):x in c]);
end while;

d:=func<p,q|Abs(p[1]-q[1])+Abs(p[2]-q[2])>;

min_x:=Min([p[1]:p in points]);
max_x:=Max([p[1]:p in points]);
min_y:=Min([p[2]:p in points]);
max_y:=Max([p[2]:p in points]);

best:={1..#points};
ngbh:=[0:p in points];

lim:=10000;
safe:=0;

for i in [min_x..max_x], j in [min_y..max_y] do
	c:=[i,j];
	dist:=[d(c,p):p in points];
	if &+dist lt lim then
		safe+:=1;
	end if;
	min,pt:=Min(dist);
	if Multiplicity(dist,min) eq 1 then
		ngbh[pt]+:=1;
		if i in {min_x,max_x} or j in {min_y,max_y} then
			Exclude(~best,pt);
		end if;
	end if;
end for;

PrintFile("day06.txt",Max({ngbh[p]:p in best}));
PrintFile("day06.txt",safe);
