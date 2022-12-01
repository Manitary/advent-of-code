F:=Open("input15.txt","r");
input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~input, [StringToInteger(x):x in Eltseq(s)]);
end while;

Y:=#input;
X:=#input[1];
scale:=5;

maxY:=Y*scale;
maxX:=X*scale;

modX:=func<x|x mod X eq 0 select X else x mod X>;
modY:=func<y|y mod Y eq 0 select Y else y mod Y>;
shift:=func<x,a|x+a gt 9 select (x+a) mod 9 else x+a>;

GetRisk:=function(y,x)
	shiftX:=(x-1) div X;
	shiftY:=(y-1) div Y;
	return shift(input[modY(y),modX(x)],shiftX+shiftY);
end function;

start:=<1,1>;
finish:=<maxY,maxX>;

NGBH:=func<p|{<p[1]+j,p[2]+i>:i,j in [-1..1]|Abs(i)+Abs(j) eq 1 and p[1]+j ge 1 and p[1]+j le maxY and p[2]+i ge 1 and p[2]+i le maxX}>;

current:={<start,0>};
visited:={start};
i:=0;
repeat
	i+:=1;
	i;
	node:=Representative({p:p in current|p[2] eq Min({x[2]:x in current})});
	Include(~visited, node[1]);
	Exclude(~current,node);
	newnodes:={<x,node[2]+GetRisk(x[1],x[2])>:x in NGBH(node[1])|x notin visited};
	for pt in newnodes do
		if exists(copy){x:x in current|x[1] eq pt[1]} then
			if pt[2] lt copy[2] then
				Exclude(~current,copy);
				Include(~current,pt);
			end if;
		else
			Include(~current,pt);
		end if;
	end for;
until exists(final){x:x in current|x[1] eq finish};

final[2];
