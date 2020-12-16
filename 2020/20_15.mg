F:=Open("input15.txt","r");

n:=[StringToInteger(x):x in Split(Gets(F),",")];
c:=#n;
t:=AssociativeArray(Integers());
for i in [1..#n] do
	t[n[i]]:=i;
end for;
last:=n[#n];
lastnew:=true;

repeat
	if lastnew then
		new:=0;
		t[last]:=c;
		last:=0;
	else
		new:=c-t[last];
		t[last]:=c;
		last:=new;
	end if;
	lastnew:=last notin Keys(t);
	c+:=1;
	if c mod 10^5 eq 0 then
		print c;
	end if;
until c eq 3*10^7;
new;
