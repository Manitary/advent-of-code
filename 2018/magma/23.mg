F:=Open("input23.txt","r");
pos:=[];
rad:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	_,p:=Regexp("[0-9,-]+",s);
	_,_,r:=Regexp("r=([0-9]+)",s);
	Append(~pos,[StringToInteger(c):c in Split(p,",")]);
	Append(~rad,StringToInteger(r[1]));
end while;

dist:=func<a,b|&+[Abs(a[i]-b[i]):i in [1..#a]]>;
inrange:=func<i,j|dist(pos[i],pos[j]) le rad[i]>;

_,idx:=Max(rad);

Multiplicity({*inrange(idx,i):i in [1..#pos]*},true);
