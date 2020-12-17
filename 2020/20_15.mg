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
	lastnew:=not IsDefined(t,last);
	c+:=1;
	if c eq 2020 then
		PrintFile("day15.txt",new);
	end if;
until c eq 3*10^7;
PrintFile("day15.txt",new);
