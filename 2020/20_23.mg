F:=Open("input23.txt","r");
cups:=[StringToInteger(x):x in Eltseq(Gets(F))];

function Fill(max)
	next:=AssociativeArray(Integers());
	prev:=AssociativeArray(Integers());
	for i in [1..#cups] do
		next[cups[i]]:=i+1 gt #cups select cups[1] else cups[i+1];
		prev[cups[i]]:=i eq 1 select cups[#cups] else cups[i-1];
	end for;
	if max gt #cups then
		for i in [#cups+1..max] do
			next[i]:=i+1;
			prev[i]:=i-1;
		end for;
		next[cups[#cups]]:=#cups+1;
		prev[#cups+1]:=cups[#cups];
		next[max]:=cups[1];
		prev[cups[1]]:=max;
	end if;
	curr:=cups[1];
	return curr, next, prev;
end function;

procedure Move(~curr,~next,~prev,max)
	pos:=curr;
	side:=[];
	for i in [1..3] do
		pos:=next[pos];
		Append(~side,pos);
	end for;
	pos:=next[pos];
	next[curr]:=pos;
	prev[pos]:=curr;
	dest:=curr eq 1 select max else curr-1;
	while dest in side do
		dest-:=1;
		if dest eq 0 then
			dest:=max;
		end if;
	end while;
	pos:=dest;
	new:=next[pos];
	next[pos]:=side[1];
	prev[side[1]]:=pos;
	next[side[3]]:=new;
	prev[new]:=side[3];
	curr:=next[curr];
end procedure;

function printcups(curr, next, prev)
	pos:=curr;
	str:="";
	repeat
		str*:=IntegerToString(pos);
		pos:=next[pos];
	until pos eq curr;
	return str;
end function;

max:=#cups;
curr,next,prev:=Fill(max);
for i in [1..100] do
	Move(~curr,~next,~prev,max);
end for;
PrintFile("day23.txt",Substring(printcups(1, next, prev),2,8));

max:=10^6;
curr,next,prev:=Fill(max);
for i in [1..10^7] do
	Move(~curr,~next,~prev,max);
end for;
PrintFile("day23.txt",next[1]*next[next[1]]);
