function ParseSnailfish(s)
	num:=[];
	depth:=[];
	d:=0;
	for i in [1..#s] do
		if s[i] eq "[" then
			d+:=1;
		elif s[i] eq "]" then
			d-:=1;
		elif s[i] eq "," then
			continue;
		else
			Append(~num,StringToInteger(s[i]));
			Append(~depth,d);
		end if;
	end for;
	return num, depth;
end function;

procedure ExplodeSnailfish(~snail, ~depth)
	for i in [1..#depth-1] do
		if depth[i] ge 5 and depth[i+1] eq depth[i] then
			if i gt 1 then
				snail[i-1]+:=snail[i];
			end if;
			if i+1 lt #snail then
				snail[i+2]+:=snail[i+1];
			end if;
			snail[i]:=0;
			Remove(~snail,i+1);
			depth[i]-:=1;
			Remove(~depth,i+1);
			break;
		end if;
	end for;
end procedure;

procedure SplitSnailfish(~snail, ~depth)
	for i in [1..#snail] do
		if snail[i] gt 9 then
			Insert(~snail, i+1, (snail[i] div 2) + (snail[i] mod 2));
			snail[i] div:=2;
			depth[i]+:=1;
			Insert(~depth, i+1, depth[i]);
			break;
		end if;
	end for;
end procedure;

procedure ReduceSnailFish(~snail,~depth)
	while Max(depth) ge 5 or Max(snail) gt 9 do
		while Max(depth) ge 5 do
			ExplodeSnailfish(~snail, ~depth);
		end while;
		if Max(snail) gt 9 then
			SplitSnailfish(~snail, ~depth);
		end if;
	end while;
end procedure;

function SnailMagnitude(snail, depth)
	s:=snail;
	d:=depth;
	while #s gt 1 do
		for i in [1..#d-1] do
			if d[i] eq d[i+1] then
				s[i]:=3*s[i]+2*s[i+1];
				d[i]-:=1;
				Remove(~s,i+1);
				Remove(~d,i+1);
				break;
			end if;
		end for;
	end while;
	return s[1];
end function;

F:=Open("input18.txt","r");
input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~input, s);
end while;

snail, depth:=ParseSnailfish(input[1]);
for i in [2..#input] do
	sn, dp:=ParseSnailfish(input[i]);
	snail cat:=sn;
	depth cat:=dp;
	depth:=[x+1:x in depth];
	ReduceSnailFish(~snail,~depth);
end for;
PrintFile("day18.txt", SnailMagnitude(snail,depth));

bestMagnitude:=0;
for snail1, snail2 in input do
	if snail1 ne snail2 then
		sn1, dp1:=ParseSnailfish(snail1);
		sn2, dp2:=ParseSnailfish(snail2);
		snail:=sn1 cat sn2;
		depth:=[x+1:x in dp1 cat dp2];
		ReduceSnailFish(~snail, ~depth);
		magnitude:=SnailMagnitude(snail,depth);
		best:=Max(bestMagnitude,magnitude);
	end if;
end for;
PrintFile("day18.txt", bestMagnitude);
