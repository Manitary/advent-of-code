F:=Open("input10.txt","r");

input:=[];

while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~input,s);
end while;

r:=#input;
c:=#input[1];

asteroids:=[[x,y]:x in [1..c],y in [1..r]|input[y,x] eq "#"];

visibility:=[{[(a[1]-b[1]) div GCD(a[1]-b[1],a[2]-b[2]),(a[2]-b[2]) div (GCD(a[1]-b[1],a[2]-b[2]))]:a in asteroids|a ne b}:b in asteroids];

sol,idx:=Max([#c:c in visibility]);
print sol;
base:=asteroids[idx];

function Arctan3(x,y)
	if x lt 0 and y ge 0 then
		return Pi(RealField())*5/2-Arctan(x,y);
	else
		return Pi(RealField())/2-Arctan(x,y);
	end if;
end function;

asteroids_rescaled:=[[a[1]-base[1],base[2]-a[2]]:a in asteroids|a ne base];

function CompareGradient(a,b)
	if Arctan3(a[1],a[2]) eq Arctan3(b[1],b[2]) then
		return Abs(a[1])+Abs(a[2])-Abs(b[1])-Abs(b[2]);
	else
		return Arctan3(a[1],a[2])-Arctan3(b[1],b[2]);
	end if;
end function;


Sort(~asteroids_rescaled,CompareGradient);

pos:=1;
for i in [1..200] do
	target:=asteroids_rescaled[pos];
	Remove(~asteroids_rescaled,pos);
	while Arctan3(asteroids_rescaled[pos,1],asteroids_rescaled[pos,2]) eq Arctan3(target[1],target[2]) do
		if pos eq #asteroids_rescaled then
			pos:=1;
		else
			pos+:=1;
		end if;
	end while;
	print target;
end for;
print target;
print (target[1]+base[1])*100+(base[2]-target[2]);
