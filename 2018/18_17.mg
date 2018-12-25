F:=Open("input17.txt","r");

clay:={};
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	_,_,y:=Regexp("y=([0-9.]+)",s);
	_,_,x:=Regexp("x=([0-9.]+)",s);
	clay join:= {Vector([a,b]):a in eval Sprint(x),b in eval Sprint(y)};
end while;

limit:=Max({v[2]:v in clay});

y:=Vector([0,1]);
x:=Vector([1,0]);

spring:=Vector([500,0]);
flow:={spring+y};
water:=flow;
rest:={};

repeat
	flow;
	w:=Random(flow);
	Exclude(~flow,w);
	while w+y notin clay and w[2] lt limit and w+y notin rest do
		w+:=y;
		Include(~water,w);
	end while;
	if w[2] lt limit then
		sides:=[w];
		blocked:=[false,false];
		while sides[1]-x notin clay and sides[1]+y in clay join rest do
			Insert(~sides,1,sides[1]-x);
		end while;
		if sides[1]-x in clay then
			blocked[1]:=true;
		end if;
		while sides[#sides]+x notin clay and sides[#sides]+y in clay join rest do
			Append(~sides,sides[#sides]+x);
		end while;
		if sides[#sides]+x in clay then
			blocked[2]:=true;
		end if;
		if &and(blocked) then
			rest join:=SequenceToSet(sides);
			Include(~flow,w-y);
		else
			water join:=SequenceToSet(sides);
			if not(blocked[1]) then
				Include(~flow,sides[1]);
			end if;
			if not(blocked[2]) then
				Include(~flow,sides[#sides]);
			end if;
		end if;
	end if;
until #flow eq 0;

PrintFile("day17.txt",#(water join rest)-Min({c[2]:c in clay})+1);
PrintFile("day17.txt",#rest);
